// add an event listener for the search button in search-coaches.html
// don't let the page refresh when the button is clicked so AJAX request can be made
// get the form data
// convert the form data into an object
// send the form data
// print the data in the console

const searchBtn = document.querySelector('#search-btn');

searchBtn.addEventListener('click', (event) => {
    event.preventDefault();

    const formData = new FormData(document.getElementById('search-coaches'));

    const searchData = {};
    formData.forEach((value, key) => {
        searchData[key] = value;
    });

    console.log(searchData);

    fetch('/search/results/coaches', {
        method: 'POST',
        body: JSON.stringify(searchData),
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        });
});