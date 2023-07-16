from flask import Flask, render_template, request, session, flash, jsonify, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import os
from functools import wraps
import secrets

secretKey = secrets.token_urlsafe(16)

app = Flask(__name__)

app.secret_key = secretKey

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged_in = session.get('logged_in', False)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    logged_in = session.get('logged_in', False)

    return render_template('catalogue.html', cards=cards_data, logged_in=logged_in)


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
        sucessful_message = "Welcome!"
        return render_template('catalogueLogged.html', cards=cards_data, sucessful_message=sucessful_message)
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
@login_required
def series_catalogue(series_name):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)
    
    logged_in = 'email' in session

    filtered_cards = [card for card in cards_data if card['series'] == series_name]

    return render_template('series_catalogue.html', cards=filtered_cards, series_name=series_name, logged_in=logged_in)

@app.route('/name/<pokemon_name>')
@login_required
def searched_catalogue(pokemon_name):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    logged_in = 'email' in session

    filtered_cards = [card for card in cards_data if card['name'] == pokemon_name]

    return render_template('searched_catalogue.html', cards=filtered_cards, pokemon_name=pokemon_name, logged_in=logged_in)

@app.route('/profiles/<card_id>')
@login_required
def profiles(card_id):
    card_profile = get_card_profile(card_id)

    logged_in = 'email' in session

    return render_template('profile.html', card=card_profile, logged_in=logged_in)

@app.route('/all_cards')
@login_required
def all_cards():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)
    
    logged_in = 'email' in session

    return render_template('all_cards.html', cards=cards_data, logged_in=logged_in)


def get_card_profile(card_id):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    for card in cards_data:
        if card['id'] == card_id:
            return card

    return None

if __name__ == "__main__":
    app.run(debug=True)