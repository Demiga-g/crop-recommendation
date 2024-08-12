document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('cropForm');
  const inputs = form.querySelectorAll('input[type="number"]');

  inputs.forEach(input => {
      input.addEventListener('input', function() {
          const value = parseFloat(this.value);
          const min = parseFloat(this.min);
          const max = parseFloat(this.max);

          if (value < min || value > max || isNaN(value)) {
              this.setCustomValidity(`Please enter a value between ${min} and ${max}`);
              this.reportValidity();
              disableNextInputs(this);
          } else {
              this.setCustomValidity('');
              enableAllInputs();
          }
      });
  });

  function disableNextInputs(currentInput) {
      let disable = false;
      inputs.forEach(input => {
          if (input === currentInput) {
              disable = true;
          } else if (disable) {
              input.disabled = true;
          }
      });
  }

  function enableAllInputs() {
      inputs.forEach(input => {
          input.disabled = false;
      });
  }

  form.addEventListener('submit', function(event) {
      let isValid = true;
      inputs.forEach(input => {
          const value = parseFloat(input.value);
          const min = parseFloat(input.min);
          const max = parseFloat(input.max);
          if (value < min || value > max || isNaN(value)) {
              isValid = false;
              input.setCustomValidity(`Please enter a value between ${min} and ${max}`);
              input.reportValidity();
          }
      });
      if (!isValid) {
          event.preventDefault();
      }
  });
});
