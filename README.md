# PokemonCardEcommerce
This project is a Flask-based mock e-commerce website for Pokémon card trading and buying. It allows users to create accounts, browse and search for Pokémon cards, add cards to their cart, manage their profile settings, pay for cart items, and more. The website simulates an online marketplace for Pokémon card enthusiasts such as ourselves to interact and engage in card transactions.

#### Table of Contents:
1. <a href="#installation-instructions">Installation Instructions</a>
2. <a href="#usage">Usage</a>
3. <a href="#demo">Demonstration</a>
4. <a href="#technologies-used">Technologies Used</a>
5. <a href="#code-examples">Code Examples</a>
6. <a href="#acknowledgments">Acknowledgments</a>
7. <a href="#contact-information">Contact Information</a>

<h2 id="installation-instructions">Installation Instructions</h2>
    
To run the Flask mock e-commerce website, follow these steps:

- Install Python 3.x on your system.
- Clone this repository to your local machine.
- Create a virtual environment using virtualenv or conda.
- Activate the virtual environment.
- Install the required dependencies by running pip install -r requirements.txt.
- Set up the database by running python db_setup.py.
- Start the Flask server by executing python app.py.
- The website will be accessible at http://localhost:5000 in your web browser.
  
<h2 id="usage">Usage</h2>
The Flask mock e-commerce website allows users to perform the following actions:

- Create an account with a unique username and password.
- Log in using their registered email and password.
- Browse and search for Pokémon cards by series and name.
- Add cards to the shopping cart and view the cart contents.
- Adjust the number of items in the cart or remove items from the cart.
- Proceed to checkout, providing delivery details and payment information.
- View order details and total value after successful checkout.
- Manage profile settings, including username, email, and password.
- View favorite Pokémon cards, payment options, and delivery details.

<h2 id="usage">Demostration</h2>

<img width="1724" alt="Screenshot 2023-07-23 at 1 34 18 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/6509db6b-483f-446c-a0bc-fe4ddd9da987">
<img width="1724" alt="Screenshot 2023-07-23 at 1 34 54 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/68cb9c05-1cfe-47b6-aa5c-8536805de1af">
<img width="1724" alt="Screenshot 2023-07-23 at 1 35 57 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/c2a45228-997c-49a9-9a4a-ddd2b39a4ba2">
<img width="1724" alt="Screenshot 2023-07-23 at 1 36 51 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/b56634f3-e204-4354-adde-cd0345d7784f">
<img width="1724" alt="Screenshot 2023-07-23 at 1 41 30 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/0e241cf1-157b-4068-8bb7-a46b47e67a5d">
<img width="496" alt="Screenshot 2023-07-23 at 1 48 53 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/8a368cff-3589-4cf5-b7c0-77867d196660">
<img width="1684" alt="Screenshot 2023-07-23 at 1 49 39 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/8e344a6b-facb-4176-8763-36b8642e25cf">
<img width="844" alt="Screenshot 2023-07-23 at 1 50 29 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/2a43158e-811e-4de4-8e3a-1939e2fb50eb">
<img width="844" alt="Screenshot 2023-07-23 at 1 51 26 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/70c1a0fd-b4b3-4c30-a882-e9c15112363a">
<img width="840" alt="Screenshot 2023-07-23 at 1 51 51 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/93f7e31f-7628-4e63-949a-acb6312620cd">
<img width="835" alt="Screenshot 2023-07-23 at 1 52 08 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/ab9f6d7b-f991-46ae-ac31-338b2f93a845">


<h2 id="technologies-used">Technologies Used</h2>
<ol>
  <li>Flask (Python Web Development Framework)</li>
  <li><a href="https://pokemontcg.io/">Pokemon TCG API</a></li>
  <li><a href="https://developer.paypal.com/api/rest/">Paypal Developer API</a></li>
  <li>Jinja (Python Templating Engine)</li>
  <li>Node.js (JSON Parsing)</li>
  <li>HTML, CSS, and JS</li>
  <li>SQLITE</li>
</ol>

<h2 id="code-examples">Code Examples</h2>
Here are some code examples to demonstrate how to use the Flask mock e-commerce website:

Example of adding a Pokémon card to the shopping cart
```
@app.route('/add_to_cart/<card_id>', methods=['POST'])
@login_required
def add_to_cart(card_id):
    # Implementation code...
    return render_template('catalogueLogged.html', user=user, cart_items=cart_items, cart_count=cart_count, total_value=total_value)
```
<h2 id="acknowledgements">Acknowledgments</h2>

The Flask mock e-commerce website was inspired by various online e-commerce platforms (beywarehouse.com) and Pokémon card trading communities.
<h2 id="contact-information">Contact Information</h2>
If you have any questions or feedback, feel free to contact us through our Contact Us form or directly emailing us, at ecommercepokemon@gmail.com. 

# Thank you for considering our Flask PokemonCardEcommerce website! If you have any further questions or need assistance, don't hesitate to reach out to us. We hope you enjoy using our platform!
