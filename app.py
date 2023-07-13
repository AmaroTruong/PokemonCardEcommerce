from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    return render_template('catalogue.html', cards=cards_data)

@app.route('/series/<series_name>')
def series_catalogue(series_name):
    file_path = os.path.join(app.static_folder, 'profiles.json')
    with open(file_path) as file:
        cards_data = json.load(file)

    filtered_cards = [card for card in cards_data if card['series'] == series_name]

    return render_template('series_catalogue.html', cards=filtered_cards, series_name=series_name)

@app.route('/profiles/<card_id>')
def profiles(card_id):
    card_profile = get_card_profile(card_id)

    return render_template('profile.html', card=card_profile)

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