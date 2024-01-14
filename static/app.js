document.getElementById('randomizeBtn').addEventListener('click', function() {
    // Make an AJAX request to the Flask server to run the Python script
    fetch('/run_python_script', { method: 'POST' })
        .then(response => response.text())
        .then(message => console.log(message))
        .catch(error => console.error('Error:', error));
});
