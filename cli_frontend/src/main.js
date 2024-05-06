document.addEventListener("DOMContentLoaded", function() {
  const decrementButtons = document.querySelectorAll("[data-hs-input-number-decrement]");
  const incrementButtons = document.querySelectorAll("[data-hs-input-number-increment]");
  const inputFields = document.querySelectorAll("[data-hs-input-number-input]");
  const buttons = document.querySelectorAll('.btn-gym_id')

// resreve button 
  buttons.forEach(btn => {
    btn.addEventListener('click', function() {
      const urlItem = '/user/gymes/' + btn.id;
      window.location.href = urlItem
    })
  })
// decrement price filter
  decrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value > 20) {
        input.value = value - 1;
      } else {
        input.value = 20; // Set to 20 if value is already 20 or NaN
      }
    });
  });
// increment the price filter
  incrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value < 150) {
        input.value = value + 1;
      } else {
        input.value = 150; // Set to 150 if value is NaN
      }
    });
  });
});
