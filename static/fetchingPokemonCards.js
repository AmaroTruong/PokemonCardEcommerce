// Define the API key for accessing the Pokemon TCG API
var apiKey = '71a213bd-22f4-4e6d-8971-5f5405ce7158';

// Define the PokemonCard class
class PokemonCard {
  constructor(cardId) {
    this.cardId = cardId;
    this.fetchCardData();
  }

  // Fetch data for the card using the Pokemon TCG API
  fetchCardData() {
    fetch(`https://api.pokemontcg.io/v2/cards/${this.cardId}`, {
      headers: {
        'X-Api-Key': apiKey
      }
    })
    .then(response => response.json())
    .then(cardData => {
      // Extract relevant data from the API response and store it in instance variables
      this.name = cardData.data.name;
      this.facts = cardData.data.nationalPokedexNumbers;
      this.imageUrl = cardData.data.images.small;
      this.series = cardData.data.set.series;
      console.log('Card:', this.name);
      
      // Try to get the market value of the card, if available, from the API response
      try {
        if (cardData.data.tcgplayer.prices.normal && cardData.data.tcgplayer.prices.normal.market) {
          this.marketValue = cardData.data.tcgplayer.prices.normal.market;
        } else if (cardData.data.tcgplayer.prices.holofoil && cardData.data.tcgplayer.prices.holofoil.market) {
          this.marketValue = cardData.data.tcgplayer.prices.holofoil.market;
        } else if (cardData.data.tcgplayer.prices['1stEditionHolofoil'] && cardData.data.tcgplayer.prices['1stEditionHolofoil'].market) {
          this.marketValue = cardData.data.tcgplayer.prices['1stEditionHolofoil'].market;
        } else if (cardData.data.tcgplayer.prices.reverseHolofoil && cardData.data.tcgplayer.prices.reverseHolofoil.market) {
          this.marketValue = cardData.data.tcgplayer.prices.reverseHolofoil.market;
        } else {
          this.marketValue = 'N/A';
        }
      } catch (error) {
        // If an error occurs while fetching the market value, set it to 'N/A'
        this.marketValue = 'N/A';
      }

      // If market value is available (not 'N/A'), create a profile for the card
      if (this.marketValue !== 'N/A') {
        this.createProfile();
      }
    });
  }

  // Create an HTML profile for the card
  createProfile() {
    var html = `
      {% extends "headerAndFooter.html" %}
      {% block title %}
      <title>${this.name} | Pokemon Cards</title>
      {% endblock %}  
      {% block header %}
      {{ super() }}
      <link rel="stylesheet" type="text/css" href="/static/cardStyling.css">
      {% endblock %}
        {% block content %}
        <img class="card-image" src="${this.imageUrl}" alt="${this.name}">
        <h2>${this.name}</h2>
        <p><strong>From:</strong> ${this.series} Series</p>
        <p><strong>Market Value:</strong> $${this.marketValue}</p>
        <p>National Pokedex Number: ${this.facts}</p>
        {% endblock %}
        {% block footer %}
        {{ super() }}
        {% endblock %}
        {% block script %}
        {{ super() }}
        <script src="/static/cardZooming.js"></script>
        {% endblock %}
    `;

    // Save the profile HTML to a repository with the cardId as the file name
    saveProfileToRepository(this.cardId, html);
  }
}

// Function to save the card profile HTML to a repository
function saveProfileToRepository(cardId, html) {
  const fs = require('fs');
  const path = require('path');

  const profilesDirectory = 'profiles';

  // Create the profiles directory if it doesn't exist
  if (!fs.existsSync(profilesDirectory)) {
    fs.mkdirSync(profilesDirectory);
  }

  // Define the path for the card's profile HTML file
  const profilePath = path.join(profilesDirectory, `${cardId}.html`);

  // Write the HTML content to the file
  fs.writeFileSync(profilePath, html);

  console.log(`Profile created for card ID ${cardId}`);
}

// Fetch the list of cards from the Pokemon TCG API and create PokemonCard instances for each card
fetch('https://api.pokemontcg.io/v2/cards')
  .then(response => response.json())
  .then(jsonData => {
    const cards = jsonData.data;

    cards.forEach(card => {
      var cardId = card.id;
      new PokemonCard(cardId);
    });
  });
