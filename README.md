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

<h1 id="usage">Demostration</h1>

## Create an Account
<img width="1724" alt="Screenshot 2023-07-24 at 12 35 19 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/7331b6dd-75fb-4db8-b511-bba6b11d4cb6">

## Log In
<img width="1724" alt="Screenshot 2023-07-24 at 12 35 41 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/0c889204-fc08-46a3-a353-3f22a91e7bfa">

## Search
<img width="1723" alt="Screenshot 2023-07-24 at 12 36 27 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/f9df0bea-3d2a-4936-b0b0-a44da0f369f5">

## Add to Cart
<img width="1711" alt="Screenshot 2023-07-24 at 12 39 15 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/ed9d505d-aa30-4531-939d-5bd3ae01a097">

## Remove From Cart
<img width="1706" alt="Screenshot 2023-07-24 at 12 39 34 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/816390ac-23a3-41c7-8557-4e4482ed19d2">

## Checkout
<img width="498" alt="Screenshot 2023-07-24 at 12 43 15 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/dd6eac72-3cdc-443a-a0f0-bb5b80770349">

## Payment Success 
<img width="1680" alt="Screenshot 2023-07-24 at 12 43 45 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/1845581a-a0a8-454c-af4a-14afcedf1a21">

## Manage Account
<img width="829" alt="Screenshot 2023-07-24 at 12 44 08 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/012609d6-dbe1-4e2c-af3d-72049101e073">

## Favorite Cards
<img width="841" alt="Screenshot 2023-07-24 at 12 44 23 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/03eed652-03b1-495e-83c9-cbe13a96ca47">

## Manage Account
<img width="817" alt="Screenshot 2023-07-24 at 12 44 37 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/d7ab2bb5-fa28-4881-8e61-74f7460a3de4">
<img width="831" alt="Screenshot 2023-07-24 at 12 44 45 AM" src="https://github.com/JackieC2027/PokemonCardEcommerce/assets/137460611/1fbfee31-bcb5-4159-b434-5a584c5f7b0b">


<h2 id="technologies-used">Technologies Used</h2>
<ul>
  <li>Flask (Python Web Development Framework)</li>
  <li><a href="https://pokemontcg.io/">Pokemon TCG API</a></li>
  <li><a href="https://developer.paypal.com/api/rest/">Paypal Developer API</a></li>
  <li>Jinja (Python Templating Engine)</li>
  <li>Node.js (JSON Parsing)</li>
  <li>HTML, CSS, and JS</li>
  <li>Docker</li>
  <li>SQLITE</li>
</ul>

# Dockerization of Website
Our Docker image is designed to host a mock e-commerce website, providing an easily deployable and scalable solution for running the application in a containerized environment. This image includes all the necessary components and dependencies required to run the mock e-commerce website seamlessly.

<h8>Windows</h8>
- Go to the Docker website: https://www.docker.com/products/docker-desktop
- Click on "Get Docker Desktop for Windows".
- The installer will be downloaded. Double-click the installer to start the installation process.
- Follow the on-screen instructions to install Docker. During installation, it might prompt you to enable Hyper-V and other necessary components. Allow the installation to make the required changes.
- Once the installation is complete, Docker should be running, and you'll see the Docker icon in the system tray.

<h8>macOS</h8>
- Go to the Docker website: https://www.docker.com/products/docker-desktop
- Click on "Get Docker Desktop for Mac".
- The installer will be downloaded. Double-click the installer to start the installation process.
- Drag and drop the Docker icon into the Applications folder to install it.
- Open Docker from the Applications folder. It might prompt you to allow the installation of additional components. Allow the installation to make the required changes.
- Once the installation is complete, Docker should be running, and you'll see the Docker icon in the menu bar.

<h8>Linux</h8>
- Docker provides different installation methods for various Linux distributions. The following are generic instructions:
- Go to the Docker website: https://docs.docker.com/engine/install/
- Choose your Linux distribution from the list of options.
- Follow the installation instructions specific to your distribution. The steps will typically involve adding Docker's official repository, installing the necessary packages, and configuring Docker to run on startup.

To pull the Docker image from the container registry, run the following command:
```docker pull amarot29/pokemonecommerce```

To run the application in a Docker container, use the following command:
```docker run -d -p 3030:3030 pokemonecommerce```

 Open your web browser and enter http://localhost to access the mock e-commerce website. Voilà! You can now explore the mock e-commerce application and test its functionalities.

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

You can email the developers at:

#### Jackie Cheng
Email: jc5187@gmail.com

#### Amaro Truong
Email: amarotruong619@gmail.com

Thank you for considering our Flask PokemonCardEcommerce website! If you have any further questions or need assistance, don't hesitate to reach out to us. We hope you enjoy using our platform!

