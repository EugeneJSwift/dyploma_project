function getMaxHeight() {
    let maxHeight = 0;
    const cardElements = document.querySelectorAll('.card');
  
    cardElements.forEach(card => {
      const cardHeight = card.offsetHeight;
      if (cardHeight > maxHeight) {
        maxHeight = cardHeight;
      }
    });
  
    return maxHeight;
  }
  
  // Функция для установки высоты всех карточек
  function setCardHeight() {
    const maxHeight = getMaxHeight();
    const cardElements = document.querySelectorAll('.card');
  
    cardElements.forEach(card => {
      card.style.height = maxHeight + 'px';
    });
  }
  
  // Вызываем функцию при загрузке страницы
  window.onload = setCardHeight; 