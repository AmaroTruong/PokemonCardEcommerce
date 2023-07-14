document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchSuggestions = document.getElementById('searchSuggestions');
  
    fetch('/static/profiles.json')
      .then(response => response.json())
      .then(data => {
        const pokemonNames = data.map(pokemon => pokemon.name);
        setupAutocomplete(pokemonNames);
      })
      .catch(error => {
        console.log('Error loading Pokemon data:', error);
      });
  
    function setupAutocomplete(pokemonNames) {
      searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.trim().toLowerCase();
        const matchingSuggestions = pokemonNames.filter(name =>
          name.toLowerCase().startsWith(searchTerm)
        );
        showSuggestions(matchingSuggestions);
      });

      document.addEventListener('click', function(event) {
        const target = event.target;
        if (target !== searchInput && !searchSuggestions.contains(target)) {
          hideSuggestions();
        }
      });
    }
  
    function showSuggestions(suggestions) {
      if (suggestions.length === 0) {
        searchSuggestions.innerHTML = '';
        return;
      }
  
      const suggestionItems = suggestions.map(suggestion => `<div class="suggestion">${suggestion}</div>`);
      searchSuggestions.innerHTML = suggestionItems.join('');
  
      const suggestionElements = document.querySelectorAll('.suggestion');
      suggestionElements.forEach(suggestionElement => {
        suggestionElement.addEventListener('click', function() {
          searchInput.value = suggestionElement.innerText;
          hideSuggestions();
        });
      });
    }
  
    function hideSuggestions() {
      searchSuggestions.innerHTML = '';
    }
  });
  