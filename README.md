# Flask Mock E-commerce Website
This project is a Flask-based mock e-commerce website for Pokémon card trading and buying. It allows users to create accounts, browse and search for Pokémon cards, add cards to their cart, manage their profile settings, pay for cart items, and more. The website simulates an online marketplace for Pokémon card enthusiasts such as ourselves to interact and engage in card transactions.

#### Table of Contents:
1. <a href="#installation-instructions">Installation Instructions</a>
2. <a href="#usage">Usage</a>
3. <a href="#technologies-used">Technologies Used</a>
4. <a href="#code-examples">Code Examples</a>
5. <a href="#acknowledgments">Acknowledgments</a>
6. <a href="#contact-information">Contact Information</a>

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
  
<h2 id="installation-instructions">Usage</h2>
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
  
<h2 id="technologies-used">Technologies Used</h2>

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

# Thank you for considering our Flask mock e-commerce website! If you have any further questions or need assistance, don't hesitate to reach out to us. We hope you enjoy using our platform!
