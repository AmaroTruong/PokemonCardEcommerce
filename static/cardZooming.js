const zoomContainer = document.querySelector(".zoomed-image");
const zoomOverlay = document.querySelector(".zoomed-overlay");
const cardImageContainer = document.querySelector(".card-image-container");
const cardImage = document.querySelector(".card-image");

cardImage.addEventListener("mousemove", (event) => {
  const imageWidth = cardImage.offsetWidth;
  const imageHeight = cardImage.offsetHeight;
  const containerWidth = cardImageContainer.offsetWidth;
  const containerHeight = cardImageContainer.offsetHeight;

  const x = event.offsetX;
  const y = event.offsetY;

  const zoomWidth = zoomContainer.offsetWidth;
  const zoomHeight = zoomContainer.offsetHeight;

  const backgroundPositionX = Math.min(Math.max(0, x - zoomWidth / 2), imageWidth - zoomWidth);
  const backgroundPositionY = Math.min(Math.max(0, y - zoomHeight / 2), imageHeight - zoomHeight);

  const scale = imageWidth / containerWidth;

  const offsetX = (x - zoomWidth / 2) * scale;
  const offsetY = (y - zoomHeight / 2) * scale;

  zoomContainer.style.backgroundImage = `url(${cardImage.src})`;
  zoomContainer.style.backgroundPosition = `${-backgroundPositionX}px ${-backgroundPositionY}px`;
  zoomContainer.style.backgroundSize = `${imageWidth}px ${imageHeight}px`;
  zoomContainer.style.transform = `scale(${scale})`;
  zoomContainer.style.left = `${x - offsetX - 50}px`;
  zoomContainer.style.top = `${y - offsetY + containerHeight - 350}px`;
  zoomContainer.style.opacity = "1";
  zoomContainer.style.display = "block";
  zoomOverlay.style.display = "block";
});

cardImage.addEventListener("mouseleave", () => {
  zoomContainer.style.opacity = "0";
  zoomContainer.style.display = "none";
  zoomOverlay.style.display = "none";
});