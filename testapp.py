import unittest
from app import app, db, User, CartCard, FavoriteCard, DeliveryDetails

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Tear down after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_homepage(self):
        # Test the homepage route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Cards', response.data)

    def test_contact_form(self):
        # Test the contact form submission
        response = self.app.post('/contact', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, Flask!'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Form submitted.', response.data)

    
    def test_create_account_success(self):
        # Test successful account creation
        response = self.app.post('/create_account', data={
            'email': 'john@example.com',
            'username': 'JohnDoe',
            'psw': 'password123'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your account was created successfully!', response.data)

        with app.app_context():
            # Check if the user was added to the database correctly
            user = User.query.filter_by(email='john@example.com').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.username, 'JohnDoe')
            self.assertEqual(user.password, 'password123')


    def test_reset_password_success(self):
        # Test successful password reset
        user = User(username='testuser', email='testuser@example.com', password='password123')
        with app.app_context():
            db.session.add(user)
            db.session.commit()

        response = self.app.post('/newPassword', data={
            'username-email': 'testuser',  
            'newpassword': 'newpassword123'  
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password was successfully changed!', response.data)

        with app.app_context():
            # Check if the password was updated in the database correctly
            updated_user = User.query.filter_by(username='testuser').first()
            self.assertEqual(updated_user.password, 'newpassword123')

    def test_add_to_cart(self):
        # Test adding an item to the cart
        email = 'jc51887@gmail.com'
        with self.app.session_transaction() as session:
            session['email'] = email

        card_id = 'hgss4-1' 
        response = self.app.post(f'/add_to_cart/{card_id}', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_increase_quantity(self):
        # Test increasing item quantity in the cart
        card_id = 'hgss4-1'
        user_id = 1
        response = self.app.post('/increase_quantity', data={
            'card_id': card_id,
            'user_id': user_id
        }, follow_redirects=True)

    def test_decrease_quantity(self):
        # Test decreasing item quantity in the cart
        card_id = 'hgss4-1'
        user_id = 1
        response = self.app.post('/decrease_quantity', data={
            'card_id': card_id,
            'user_id': user_id
        }, follow_redirects=True)


    def test_add_to_favorites(self):
        # Test adding an item to favorites
        email = 'jc51887@gmail.com'
        with self.app.session_transaction() as session:
            session['email'] = email
            session['logged_in'] = True

        card_id = 'hgss4-1'

        with app.app_context():
            user = User.query.filter_by(email=email).first()

            if user is None:
                user = User(email=email, username='test_user', password='password123')
                db.session.add(user)
                db.session.commit()
                user = User.query.filter_by(email=email).first()  
            user_id = user.id
            new_card = FavoriteCard(user_id=user_id, card_id=card_id, series="testSeries", name="testCard", price=100.0, facts="test facts", imageUrl="testurl")
            db.session.add(new_card)
            db.session.commit()

        response = self.app.post(f'/profiles/{card_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        with app.app_context():
            # Check if the card was removed from favorites correctly
            card = FavoriteCard.query.filter_by(card_id=card_id, user_id=user_id).first()
            self.assertIsNone(card)  


if __name__ == '__main__':
    unittest.main()




