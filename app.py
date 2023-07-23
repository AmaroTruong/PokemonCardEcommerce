from flask import Flask, render_template, request, session, flash, jsonify, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import os
from functools import wraps
import secrets
from flask_mail import Mail, Message
from flask_caching import Cache
from sqlalchemy.orm import Session
from flask_migrate import Migrate
import paypalrestsdk


secretKey = secrets.token_urlsafe(16)

cache = Cache()

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300
cache.init_app(app)

app.secret_key = secretKey

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

paypalrestsdk.configure({
  "mode": "sandbox", 
  "client_id": "AUr0qn9zYIZ6dluk0ecGxc4WEcBrInsPhyDEMdHWp-wj5LPPaZxZm8_ZMMjdU9ltqs8ImKQ0ueJbiakW",
  "client_secret": "EIcOVtwfi9W8C7K-QlZoJ5MR6ZKV-LjjKjYPNXHN5MAfHl3fWtN4Ojd6-dHHRE_6e1ocJeRgXMJE9vlL" })

migrate = Migrate(app, db)

class CartCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.String(100), nullable=False)
    series = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)

class PaymentOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    cardholder_name = db.Column(db.String(100), nullable=False)
    expiration_date = db.Column(db.String(5), nullable=False)
    cvv_number = db.Column(db.String(4), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    delivery_details = db.relationship('DeliveryDetails', backref='user', uselist=False)
    cart_cards = db.relationship('CartCard', backref='user', lazy=True)
    favorite_cards = db.relationship('FavoriteCard', backref='user', lazy=True)
    payments = db.relationship('PaymentOption', backref='user', lazy=True)

class DeliveryDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

class FavoriteCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.String(100), nullable=False)
    series = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    facts = db.Column(db.String(255), nullable=True)
    imageUrl = db.Column(db.String(255), nullable=True)

with app.app_context():
    db.create_all()

app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'companygojim@gmail.com',
    MAIL_PASSWORD = 'znowewnnfmgdisvy',
))

mail = Mail(app)

@app.route('/payment', methods=['POST'])
def payment():

    user = None
    cart_items = None
    cart_count = None
    total_value = None
    payment_options = None
    delivery_details = None

    logged_in = session.get('logged_in', False)
    email = session.get('email')
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = round(sum(item.price * item.quantity for item in cart_items),2)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:3030/payment/execute",
            "cancel_url": "http://localhost:3030/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": 'Entire Cart',
                    "sku": "12345",
                    "price": total_value,
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": total_value,
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        print('Payment success!')
        session['payment_initiated'] = True
    else:
        print(payment.error)

    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():

    user = None
    cart_items = None
    cart_count = None
    total_value = None
    payment_options = None
    delivery_details = None

    logged_in = session.get('logged_in', False)
    email = session.get('email')

    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = 0
        total_value = 0
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    success = False

    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id': request.form['payerID']}):
        success = True
        successMessage = 'Thank you for ordering at PokeFinder.com!'
        # Build a dictionary with the relevant data to pass as a JSON response
        response_data = {
            'success': True,
            'redirect_url': url_for('index', cart_items=cart_items, user=user, cart_count=cart_count, payment_options=payment_options, delivery_details=delivery_details, successMessage=successMessage)
        }
    else:
        response_data = {'success': False}

    return jsonify(response_data)

@app.route('/executeRefresh')
def execute_Refresh():
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    user = None
    cart_items = None
    cart_count = None
    total_value = None
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        for cart_item in cart_items:
            db.session.delete(cart_item)
        db.session.commit()
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = round(sum(item.price * item.quantity for item in cart_items),2)
    sucessMessage = 'Thank you for ordering at PokeFinder.com!'
    return redirect(url_for('paymentSucess', sucessMessage=sucessMessage, cart_count=cart_count, cart_items=cart_items, total_value=total_value, user=user, logged_in=logged_in))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        cart_count = 0
        total_value = 0
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')
        
        msg = Message("New message from your Flask app",
                      sender=email,
                      recipients=["ecommercepokemon@gmail.com"])
        msg.body = f"""
        From: {name} <{email}>
        {user_message}
        """
        mail.send(msg)

        formMessage = "Form submitted."
        return render_template('contact.html', formMessage=formMessage, cart_count=cart_count, total_value=total_value, cart_items=cart_items, logged_in=logged_in)
    return render_template('contact.html', cart_count=cart_count, total_value=total_value, cart_items=cart_items, logged_in=logged_in)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged_in = session.get('logged_in', False)
        if not logged_in:
            flash("You must be logged in to access this feature.")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/paymentSucess')
@login_required
def paymentSucess():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    logged_in = session.get('logged_in', False)
    email = session.get('email')

    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0
        payment_options = None
        delivery_details = None

    total_value = sum(item.price * item.quantity for item in cart_items)
    notLoggedInMessage = session.pop('_flashes', None)
    return render_template('paymentSucess.html',user=user,cart_items=cart_items,cart_count=cart_count,payment_options=payment_options,delivery_details=delivery_details,total_value=total_value,notLoggedInMessage=notLoggedInMessage,logged_in=logged_in)

@app.route('/decrease_quantity', methods=['POST', 'GET'])
@login_required
def decrease_quantity():
    if request.method == 'POST':
        card_id = request.form.get('card_id')
        email = session.get('email')
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards

        cart_card = CartCard.query.filter_by(card_id=card_id, user_id=user.id).first()

        if cart_card.quantity > 1:
            cart_card.quantity -= 1
            db.session.commit()
        else:
            db.session.delete(cart_card)
            db.session.commit()
            return redirect(url_for('index'))

        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    return render_template('catalogueLogged.html', user=user, favorite_cards=user.favorite_cards, cards=cards_data, cart_items=cart_items, cart_count=cart_count, total_value=total_value)

@app.route('/update_quantity/<card_id>', methods=['GET', 'POST'])
@login_required
def update_quantity(card_id):
    if request.method == 'POST':
        email = session.get('email')
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        card_id = request.form.get('card_id')
        selected_quantity = int(request.form.get('quantity', 1))
        cart_card = CartCard.query.filter_by(card_id=card_id, user_id=user.id).first()
        card_profile = get_card_profile(card_id)

        if cart_card is None:
            cart_card = CartCard(
            user_id=user.id,
            card_id=card_id,
            series=card_profile['series'],
            name=card_profile['name'],
            price=card_profile['marketValue'],
            imageUrl = card_profile['imageUrl'],
            quantity=selected_quantity
        )
            db.session.add(cart_card)
        else:
            cart_card.quantity += selected_quantity
        db.session.commit()

        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    return redirect(url_for('profiles', card_id=card_id, favorite_cards=user.favorite_cards, user=user, cards=cards_data, cart_items=cart_items, cart_count=cart_count, total_value=total_value))

@app.route('/increase_quantity', methods=['GET', 'POST'])
@login_required
def increase_quantity():
    if request.method == 'POST':
        email = session.get('email')
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        card_id = request.form.get('card_id')

        cart_card = CartCard.query.filter_by(card_id=card_id, user_id=user.id).first()

        cart_card.quantity += 1
        db.session.commit()

        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    return render_template('catalogueLogged.html', favorite_cards=user.favorite_cards, user=user, cards=cards_data, cart_items=cart_items, cart_count=cart_count, total_value=total_value)

@app.route('/newPassword', methods=['POST'])
def reset_password():

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    username_email = request.form.get('username-email')
    user = User.query.filter((User.username == username_email) | (User.email == username_email)).first()
    if request.method == 'POST':
        new_password = request.form.get('newpassword')
        if new_password:
            user.password = new_password
            db.session.commit()
    passwordChange = "Password was successfully changed!"
    return render_template('catalogue.html', cards=cards_data, passwordChange=passwordChange)

    
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    currentRoute = 'settings'
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    cart_items = user.cart_cards
    cart_count = sum(cart_item.quantity for cart_item in cart_items)
    payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
    total_value = sum(item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        new_password = request.form.get('password')

        user.username = new_username
        user.email = new_email
        user.password = new_password
        db.session.commit()

    return render_template('settingsUser.html', currentRoute=currentRoute, user=user, favorite_cards=user.favorite_cards, payment_options=payment_options, cart_count=cart_count, delivery_details=delivery_details, total_value=total_value, cart_items=cart_items)

@app.route('/profiles/<card_id>', methods=['POST'])
@login_required
def add_to_favorites(card_id):
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    favorite_card = FavoriteCard.query.filter_by(card_id=card_id, user_id=user.id).first()

    if favorite_card:
        db.session.delete(favorite_card)
    else:
        card_profile = get_card_profile(card_id)
        favorite_card = FavoriteCard(
            user_id=user.id,
            card_id=card_id,
            series=card_profile['series'],
            name=card_profile['name'],
            price=card_profile['marketValue'],
            facts=int(card_profile['facts'][0]),
            imageUrl=card_profile['imageUrl']
        )
        db.session.add(favorite_card) 
    db.session.commit()
    notLoggedInMessage = session.pop('_flashes', None)
    return redirect(url_for('profiles', card_id=card_id, notLoggedInMessage=notLoggedInMessage))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/settings/delivery', methods=['POST'])
@login_required
def save_settings():
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    currentRoute = "settingsD"
    cart_items = user.cart_cards
    cart_count = sum(cart_item.quantity for cart_item in cart_items)
    total_value = sum(item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        selected_option_value = request.form.get('selected-option-value')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        country = request.form.get('country')
        city = request.form.get('city')
        zip_code = request.form.get('zip-code')
        phone_number = request.form.get('phone-number')

        if selected_option_value == "0":
            delivery_detail = DeliveryDetails(
                address1=address1,
                address2=address2,
                country=country,
                city=city,
                zip_code=zip_code,
                phone_number=phone_number,
                user_id=user.id
            )
            db.session.add(delivery_detail)
        else:
            delivery_detail = db.session.query(DeliveryDetails).filter_by(id=selected_option_value).first()
            
            if delivery_detail:
                delivery_detail.address1 = address1
                delivery_detail.address2 = address2
                delivery_detail.country = country
                delivery_detail.city = city
                delivery_detail.zip_code = zip_code
                delivery_detail.phone_number = phone_number

        db.session.commit()

        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()

    return render_template('settingsUser.html', payment_options=payment_options, favorite_cards=user.favorite_cards, currentRoute=currentRoute, user=user, delivery_details=delivery_details, cart_count=cart_count, cart_items=cart_items, total_value=total_value)

@app.route('/settings/payment', methods=['POST'])
@login_required
def save_payment_option():
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    currentRoute = "settingsP"
    cart_items = user.cart_cards
    cart_count = sum(cart_item.quantity for cart_item in cart_items)
    total_value = sum(item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        selected_option_value = request.form.get('payment')
        card_number = request.form.get('card-number')
        cardholder_name = request.form.get('card-name')
        expiration_date = request.form.get('expiration-date')
        cvv_number = request.form.get('cvv')

        if selected_option_value == "0":
            payment_option = PaymentOption(
                user_id=user.id,
                card_number=card_number,
                cardholder_name=cardholder_name,
                expiration_date=expiration_date,
                cvv_number=cvv_number
            )
            db.session.add(payment_option)
        else:
            payment_option = PaymentOption.query.filter_by(id=selected_option_value, user_id=user.id).first()

            if payment_option:
                payment_option.card_number = card_number
                payment_option.cardholder_name = cardholder_name
                payment_option.expiration_date = expiration_date
                payment_option.cvv_number = cvv_number

        db.session.commit()

        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()

    return render_template('settingsUser.html', currentRoute=currentRoute, favorite_cards=user.favorite_cards, user=user, delivery_details=delivery_details, payment_options=payment_options, cart_items=cart_items, cart_count=cart_count, total_value=total_value)

@app.route('/add_to_cart/<card_id>', methods=['POST'])
@login_required
def add_to_cart(card_id):
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    cart_card = CartCard.query.filter_by(card_id=card_id).first()
    cart_items = user.cart_cards
    card_profile = get_card_profile(card_id)

    if cart_card:
        cart_card.quantity += 1
    else:
        card_profile = get_card_profile(card_id)
        cart_card = CartCard(
            user_id=user.id,
            card_id=card_id,
            series=card_profile['series'],
            name=card_profile['name'],
            price=card_profile['marketValue'],
            imageUrl = card_profile['imageUrl'],
            quantity=1
        )
        db.session.add(cart_card)

    db.session.commit()

    cart_items = user.cart_cards

    cart_count = sum(cart_item.quantity for cart_item in cart_items)
    total_value = sum(item.price * item.quantity for item in cart_items)
    notLoggedInMessage = session.pop('_flashes', None)
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    return render_template('catalogueLogged.html', user=user, cards=cards_data, favorite_cards=user.favorite_cards, cart_items=cart_items, cart_count=cart_count, total_value=total_value, notLoggedInMessage=notLoggedInMessage)


@app.route('/')
def index():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    logged_in = session.get('logged_in', False)
    email = session.get('email')
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0
        payment_options = None
        delivery_details = None
    
    total_value = sum(item.price * item.quantity for item in cart_items)
    notLoggedInMessage = session.pop('_flashes', None)

    return render_template('catalogue.html', cards=cards_data, logged_in=logged_in, payment_options=payment_options, delivery_details=delivery_details, cart_count=cart_count, cart_items=cart_items, total_value=total_value, notLoggedInMessage=notLoggedInMessage)


@app.route('/catalogue', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['psw']

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    userValidation = User.query.filter_by(email=email, password=password).first()

    if userValidation:
        user = User.query.filter_by(email=email).first()
        session['email'] = email
        session['username'] = user.username
        session['logged_in'] = True
        session['token'] = secrets.token_urlsafe(16)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
        cart_items = user.cart_cards if 'email' in session else []
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        sucessful_message = "Welcome!"
        return render_template('catalogueLogged.html', cards=cards_data, payment_options=payment_options, delivery_details=delivery_details, sucessful_message=sucessful_message, user=user, cart_count=cart_count, cart_items=cart_items, total_value=total_value)
    else:
        error_message = "Password or email is incorrect. Please try again."
        return render_template('catalogue.html', cards=cards_data, error_message=error_message)
    
@app.route('/create_account', methods=['POST'])
def create_account():

    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    email = request.form['email']
    username = request.form['username']
    password = request.form['psw']

    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    message = "Your account was created successfully!"
    return render_template('catalogue.html', message=message, cards=cards_data)

@app.route('/series/<series_name>')
def series_catalogue(series_name):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)
    user = None
    cart_items = None
    cart_count = None
    total_value = None
    payment_options = None
    delivery_details = None
    
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()

    filtered_cards = [card for card in cards_data if card['series'] == series_name]
    notLoggedInMessage = session.pop('_flashes', None)

    return render_template('series_catalogue.html', payment_options=payment_options, delivery_details=delivery_details, notLoggedInMessage=notLoggedInMessage, cards=filtered_cards, series_name=series_name, logged_in=logged_in, cart_items=cart_items, user=user, cart_count=cart_count, total_value=total_value)

@app.route('/name/<pokemon_name>')
def searched_catalogue(pokemon_name):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    logged_in = session.get('logged_in', False)
    email = session.get('email')
    user = None
    total_value = 0
    payment_options = None
    delivery_details = None
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0

    filtered_cards = [card for card in cards_data if card['name'] == pokemon_name]
    notLoggedInMessage = session.pop('_flashes', None)

    return render_template('searched_catalogue.html', notLoggedInMessage=notLoggedInMessage, payment_options=payment_options, delivery_details=delivery_details, cards=filtered_cards, pokemon_name=pokemon_name, logged_in=logged_in, cart_count=cart_count, cart_items=cart_items, user=user, total_value=total_value)

@app.route('/profiles/<card_id>')
def profiles(card_id):

    logged_in = session.get('logged_in', False)
    email = session.get('email')
    card_profile = get_card_profile(card_id)
    notLoggedInMessage = session.pop('_flashes', None)
    is_favorite = False
    user = None
    delivery_details = None
    payment_options = None
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        favorite_card = FavoriteCard.query.filter_by(card_id=card_id, user_id=user.id).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
        if favorite_card:
            is_favorite = True
        else:
            is_favorite = False
    else:
        cart_items = []
        cart_count = 0
        total_value = 0

    return render_template('profile.html', notLoggedInMessage=notLoggedInMessage, payment_options=payment_options, delivery_details=delivery_details, card=card_profile, is_favorite=is_favorite, logged_in=logged_in, cart_items=cart_items, cart_count=cart_count, user=user, total_value=total_value,_external=True)

@app.route('/all_cards')
def all_cards():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)
    
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    cart_items = []
    cart_count = 0
    total_value = 0
    user = None
    payment_options = None
    delivery_details = None
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0
    notLoggedInMessage = session.pop('_flashes', None)

    print(cart_count)
    return render_template('all_cards.html', payment_options=payment_options, delivery_details=delivery_details, notLoggedInMessage=notLoggedInMessage, cards=cards_data, logged_in=logged_in, cart_count=cart_count, cart_items=cart_items, user=user, total_value=total_value)
 
def get_card_profile(card_id):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    for card in cards_data:
        if card['id'] == card_id:
            return card

    return None

@app.route('/about')
def about():
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0
        total_value = 0
        payment_options = None
        delivery_details = None
    return render_template('about.html', cart_count=cart_count, total_value=total_value, cart_items=cart_items, logged_in=logged_in, payment_options=payment_options, delivery_details=delivery_details)

@app.route('/privacy')
def privacy():
    logged_in = session.get('logged_in', False)
    email = session.get('email')
    
    if logged_in and email:
        user = User.query.filter_by(email=email).first()
        cart_items = user.cart_cards
        cart_count = sum(cart_item.quantity for cart_item in cart_items)
        total_value = sum(item.price * item.quantity for item in cart_items)
        payment_options = PaymentOption.query.filter_by(user_id=user.id).all()
        delivery_details = DeliveryDetails.query.filter_by(user_id=user.id).all()
    else:
        cart_items = []
        cart_count = 0
        total_value = 0
        payment_options = None
        delivery_details = None
    return render_template('privacy.html', cart_count=cart_count, total_value=total_value, cart_items=cart_items, logged_in=logged_in, payment_options=payment_options, delivery_details=delivery_details)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3030)
