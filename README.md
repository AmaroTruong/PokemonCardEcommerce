# PokemonCardEcommerce
    <h1>Project Description:</h1>
    <p>
        This project is a Flask-based mock ecommerce website for Pokémon card trading and buying. It allows users to create accounts, browse and search for Pokémon cards, add cards to their cart, manage their profile settings, view order details, and more. The website simulates an online marketplace for Pokémon card enthusiasts to interact and engage in card transactions.
    </p>

    <h2>Table of Contents:</h2>
    <ul>
        <li>Installation Instructions</li>
        <li>Usage</li>
        <li>Configuration</li>
        <li>Features</li>
        <li>Documentation</li>
        <li>Contributing Guidelines</li>
        <li>Code Examples</li>
        <li>License</li>
        <li>Acknowledgments</li>
        <li>Badges</li>
        <li>Contact Information</li>
        <li>Troubleshooting</li>
        <li>Changelog</li>
        <li>FAQ</li>
        <li>Demo</li>
    </ul>

    <h2>Installation Instructions:</h2>
    <p>
        To run the Flask mock ecommerce website, follow these steps:
    </p>
    <ol>
        <li>Install Python 3.x on your system.</li>
        <li>Clone this repository to your local machine.</li>
        <li>Create a virtual environment using virtualenv or conda.</li>
        <li>Activate the virtual environment.</li>
        <li>Install the required dependencies by running <code>pip install -r requirements.txt</code>.</li>
        <li>Set up the database by running <code>python db_setup.py</code>.</li>
        <li>Start the Flask server by executing <code>python app.py</code>.</li>
        <li>The website will be accessible at <a href="http://localhost:5000">http://localhost:5000</a> in your web browser.</li>
    </ol>

    <h2>Usage:</h2>
    <p>
        The Flask mock ecommerce website allows users to perform the following actions:
    </p>
    <ul>
        <li>Create an account with a unique username and password.</li>
        <li>Log in using their registered email and password.</li>
        <li>Browse and search for Pokémon cards by series and name.</li>
        <li>Add cards to the shopping cart and view the cart contents.</li>
        <li>Adjust the quantity of items in the cart or remove items from the cart.</li>
        <li>Proceed to checkout, providing delivery details and payment information.</li>
        <li>View order details and total value after successful checkout.</li>
        <li>Manage profile settings, including username, email, and password.</li>
        <li>View favorite Pokémon cards, payment options, and delivery details.</li>
    </ul>

    <h2>Configuration:</h2>
    <p>
        The Flask mock ecommerce website uses the configuration settings specified in the config.py file. Ensure that the database URL, secret key, and other environment-specific configurations are correctly set before running the application.
    </p>

    <h2>Features:</h2>
    <ul>
        <li>User Authentication and Account Creation</li>
        <li>Pokémon Card Catalogue and Search</li>
        <li>Shopping Cart Management</li>
        <li>Checkout and Order Confirmation</li>
        <li>User Profile Settings</li>
        <li>Favorite Pokémon Cards</li>
        <li>Payment Options and Delivery Details</li>
    </ul>

    <h2>Documentation:</h2>
    <p>
        For detailed documentation on using the Flask mock ecommerce website, refer to the <a href="docs/">docs folder</a> in the repository.
    </p>

    <h2>Contributing Guidelines:</h2>
    <p>
        Contributions to the project are welcome! If you wish to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.
    </p>

    <h2>Code Examples:</h2>
    <p>
        Here are some code examples to demonstrate how to use the Flask mock ecommerce website:
    </p>
    <pre><code>
        # Example of adding a Pokémon card to the shopping cart
        @app.route('/add_to_cart/<card_id>', methods=['POST'])
        @login_required
        def add_to_cart(card_id):
            # Implementation code...
            return render_template('catalogueLogged.html', user=user, cart_items=cart_items, cart_count=cart_count, total_value=total_value)
    </code></pre>

    <h2>License:</h2>
    <p>
        This project is licensed under the MIT License. See the LICENSE file for more details.
    </p>

    <h2>Acknowledgments:</h2>
    <p>
        The Flask mock ecommerce website was inspired by various online ecommerce platforms and Pokémon card trading communities.
    </p>

    <h2>Contact Information:</h2>
    <p>
        If you have any questions or feedback, feel free to contact us at <a href="mailto:support@ecommercepokefinder.com">support@ecommercepokefinder.com</a>.
    </p>

    <h2>Troubleshooting:</h2>
    <p>
        If you encounter any issues or errors while using the website, please refer to the Troubleshooting section in the documentation.
    </p>

    <h2>Changelog:</h2>
    <p>
        v1.0.0 (2023-07-22): Initial release of the Flask mock ecommerce website.
    </p>

    <h2>FAQ:</h2>
    <p>
        Q: How do I reset my password?<br>
        A: Click on the "Forgot Password" link on the login page and follow the instructions to reset your password.
    </p>

    <h2>Demo:</h2>
    <p>
        Click <a href="#">here</a> to view a live demo of the Flask mock ecommerce website.
    </p>

    <p>
        Thank you for considering our Flask mock ecommerce website! If you have any further questions or need assistance, don't hesitate to reach out to us. We hope you enjoy using our platform!
    </p>
</body>
</html>