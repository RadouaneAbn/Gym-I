document.addEventListener("DOMContentLoaded", function() {
  const decrementButtons = document.querySelectorAll("[data-hs-input-number-decrement]");
  const incrementButtons = document.querySelectorAll("[data-hs-input-number-increment]");
  const inputFields = document.querySelectorAll("[data-hs-input-number-input]");
  const buttons = document.querySelectorAll('.btn-gym_id')

  buttons.forEach(btn => {
    btn.addEventListener('click', function() {
      const urlItem = '/user/gymes/' + btn.id;
      window.location.href = urlItem
    })
  })

  decrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value > 20 && value < 150) {
        input.value = value - 10;
      } else {
        input.value = 20; // Set to 0 if value is already 0 or NaN
      }
    });
  });

  incrementButtons.forEach(button => {
    button.addEventListener("click", function() {
      const input = this.parentElement.querySelector("[data-hs-input-number-input]");
      let value = parseInt(input.value);
      if (!isNaN(value) && value < 150 && value > 20) {
        input.value = value + 20;
      } else {
        input.value = 150; // Set to 1 if value is NaN
      }
    });
  });
});
