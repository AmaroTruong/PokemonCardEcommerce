var apiKey = '71a213bd-22f4-4e6d-8971-5f5405ce7158';

class PokemonCard {
  constructor(cardId) {
    this.cardId = cardId;
    this.fetchCardData();
  }

  fetchCardData() {
    fetch(`https://api.pokemontcg.io/v2/cards/${this.cardId}`, {
      headers: {
        'X-Api-Key': apiKey
      }
    })
    .then(response => response.json())
    .then(cardData => {
      this.name = cardData.data.name;
      this.facts = cardData.data.nationalPokedexNumbers;
      this.imageUrl = cardData.data.images.small;
      this.series = cardData.data.set.series;
      console.log('Card:', this.name);
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
      this.marketValue = 'N/A';
    }

      if (this.marketValue !== 'N/A') {
        this.createProfile();
      }
    });
  }

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

    saveProfileToRepository(this.cardId, html);
  }
}

function saveProfileToRepository(cardId, html) {
  const fs = require('fs');
  const path = require('path');

  const profilesDirectory = 'profiles';

  if (!fs.existsSync(profilesDirectory)) {
    fs.mkdirSync(profilesDirectory);
  }

  const profilePath = path.join(profilesDirectory, `${cardId}.html`);

  fs.writeFileSync(profilePath, html);

  console.log(`Profile created for card ID ${cardId}`);
}

fetch('https://api.pokemontcg.io/v2/cards')
  .then(response => response.json())
  .then(jsonData => {
    const cards = jsonData.data;

    cards.forEach(card => {
      var cardId = card.id;
      new PokemonCard(cardId);
    });
  });
