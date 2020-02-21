const form = document.getElementById('form');
const classification = document.getElementById('classification');

form.addEventListener('submit', event => {
  fetchClassification();
  event.preventDefault();
})

function fetchClassification() {
  fetch('http://localhost/classify', {
    method: "POST",
    body: new FormData(form)
  }).then(response => {
    if (response.status !== 200) {
      throw Error(`${response.status} error fetching class`);
    }
    return response.json().then(res => res.class);
  }).then(result => {
    classification.textContent = `Class: ${result}`;
  }).catch(e => {
    classification.textContent = 'Couldn\'t perform classification';
  });
}
