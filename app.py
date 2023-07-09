from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import secrets

secretKey = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secretKey
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'


db = SQLAlchemy(app)
class Card(db.Model):
    id = db.Column('card_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    generation = db.Column(db.String(100))
    card_image = db.Column(db.String(200))
    price = db.Column(db.Float)

def __init__(self, name, generation, card_image, price):
   self.name = name
   self.generation = generation
   self.card_image = card_image
   self.price = price

db.create_all()


@app.route('/')
def index():
    return render_template('catalogue.html')

if __name__ == "__main__":
    app.run(debug=True)