// Wait for the DOM content to be loaded before executing the code
document.addEventListener('DOMContentLoaded', function() {
  // Get references to the search input and the search suggestions container
  const searchInput = document.getElementById('searchInput');
  const searchSuggestions = document.getElementById('searchSuggestions');

  // Fetch Pokemon data from the profiles.json file and set up autocomplete functionality
  fetch('/static/profiles.json')
    .then(response => response.json())
    .then(data => {
      // Extract an array of Pokemon names from the fetched data
      const pokemonNames = data.map(pokemon => pokemon.name);
      // Call the setupAutocomplete function to enable autocomplete for the search input
      setupAutocomplete(pokemonNames);
    })
    .catch(error => {
      // Handle any errors that occurred during the fetch process
      console.log('Error loading Pokemon data:', error);
    });

  // Function to set up autocomplete for the search input using the provided Pokemon names
  function setupAutocomplete(pokemonNames) {
    // Add an input event listener to the search input to trigger the autocomplete functionality
    searchInput.addEventListener('input', function() {
      // Get the trimmed and lowercased search term from the input
      const searchTerm = searchInput.value.trim().toLowerCase();
      // Filter the Pokemon names to find the ones that start with the search term
      const matchingSuggestions = pokemonNames.filter(name =>
        name.toLowerCase().startsWith(searchTerm)
      );
      // Display the filtered suggestions in the search suggestions container
      showSuggestions(matchingSuggestions);
    });

    // Add a click event listener to the document to detect clicks outside the search input and suggestions container
    document.addEventListener('click', function(event) {
      const target = event.target;
      // If the click is not on the search input or within the suggestions container, hide the suggestions
      if (target !== searchInput && !searchSuggestions.contains(target)) {
        hideSuggestions();
      }
    });
  }

  // Function to display the autocomplete suggestions based on the provided list of suggestions
  function showSuggestions(suggestions) {
    // If there are no matching suggestions, clear the search suggestions container and return
    if (suggestions.length === 0) {
      searchSuggestions.innerHTML = '';
      return;
    }

    // Create HTML elements for each suggestion and join them into a single string
    const suggestionItems = suggestions.map(suggestion => `<div class="suggestion">${suggestion}</div>`);
    // Set the search suggestions container's HTML content to the joined string of suggestion items
    searchSuggestions.innerHTML = suggestionItems.join('');

    // Get references to the suggestion elements and add click event listeners to each
    const suggestionElements = document.querySelectorAll('.suggestion');
    suggestionElements.forEach(suggestionElement => {
      suggestionElement.addEventListener('click', function() {
        // When a suggestion is clicked, set the search input's value to the clicked suggestion
        searchInput.value = suggestionElement.innerText;
        // Hide the suggestions after a suggestion is selected
        hideSuggestions();
      });
    });
  }

  // Function to hide the search suggestions by clearing the HTML content of the container
  function hideSuggestions() {
    searchSuggestions.innerHTML = '';
  }
});
