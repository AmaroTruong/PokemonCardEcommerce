// Selecting the necessary elements from the DOM
const zoomContainer = document.querySelector(".zoomed-image");
const zoomOverlay = document.querySelector(".zoomed-overlay");
const cardImageContainer = document.querySelector(".card-image-container");
const cardImage = document.querySelector(".card-image2");

// Adding a mousemove event listener to the cardImage element
cardImage.addEventListener("mousemove", (event) => {
  // Get dimensions of the cardImage and cardImageContainer
  const imageWidth = cardImage.offsetWidth;
  const imageHeight = cardImage.offsetHeight;
  const containerWidth = cardImageContainer.offsetWidth;
  const containerHeight = cardImageContainer.offsetHeight;

  // Get mouse cursor position relative to the cardImage element
  const x = event.offsetX;
  const y = event.offsetY;

  // Calculate the dimensions of the zoomed image container
  const zoomWidth = zoomContainer.offsetWidth;
  const zoomHeight = zoomContainer.offsetHeight;

  // Calculate the background position of the zoomed image
  const backgroundPositionX = Math.min(Math.max(0, x - zoomWidth / 2), imageWidth - zoomWidth);
  const backgroundPositionY = Math.min(Math.max(0, y - zoomHeight / 2), imageHeight - zoomHeight);

  // Calculate the scale for the zoomed image
  const scale = imageWidth / containerWidth;

  // Calculate the offset for the zoomed image based on mouse position
  const offsetX = (x - zoomWidth / 2) * scale;
  const offsetY = (y - zoomHeight / 2) * scale;

  // Set the background image and position of the zoomed image container
  zoomContainer.style.backgroundImage = `url(${cardImage.src})`;
  zoomContainer.style.backgroundPosition = `${-backgroundPositionX}px ${-backgroundPositionY}px`;
  zoomContainer.style.backgroundSize = `${imageWidth}px ${imageHeight}px`;

  // Apply scale and position to the zoomed image container
  zoomContainer.style.transform = `scale(${scale})`;
  zoomContainer.style.left = `${x - offsetX - 50}px`;
  zoomContainer.style.top = `${y - offsetY + containerHeight - 350}px`;

  // Show the zoomed image container and overlay
  zoomContainer.style.opacity = "1";
  zoomContainer.style.display = "block";
  zoomOverlay.style.display = "block";
});

// Adding a mouseleave event listener to the cardImage element
cardImage.addEventListener("mouseleave", () => {
  // Hide the zoomed image container and overlay
  zoomContainer.style.opacity = "0";
  zoomContainer.style.display = "none";
  zoomOverlay.style.display = "none";
});
