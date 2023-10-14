
// let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
// let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
//   return new bootstrap.Tooltip(tooltipTriggerEl);
// });


const accordionButtons = document.querySelectorAll('.accordionButton');
  accordionButtons.forEach(button => {
    button.addEventListener('click', () => {
      const icon = button.querySelector('.arrow-down');
      icon.classList.toggle('fa-rotate-180');
    });
  });