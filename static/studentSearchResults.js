// add an event listener for the search button in search-coaches.html
// don't let the page refresh when the button is clicked so AJAX request can be made
// get the form data
// convert the form data into an object
// send the form data
// print the data in the console

// Create a function to display the results on a page
// Needs a container in the html file to insert the results
// Loop through the search results, create html elements to display data

const displayResults = (searchResults) => {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = "";

    searchResults.forEach((result) => {
        resultElement = document.createElement('div');
        resultElement.classList.add('profile-card');
        messageBtn = document.createElement('button')
        messageBtn.innerText = 'Send SMS'
        resultElement.innerHTML = (
            `Coach: ${result.fname} ${result.lname}<br>`
            + `School: ${result.school_id}<br>`
            + `Sport: ${result.sport_name}<br>`
            + `Bio: ${result.bio}<br>`
            + `Email: <a href="mailto:${result.coach_email}">${result.coach_email}</a><br>`
            // create element for button and add into the loop
        );
        resultElement.appendChild(messageBtn)
        messageBtn.addEventListener('click', (event) => {
            fetch('/send_coach_sms', {
                method: 'POST',
                body: JSON.stringify({studentMsg: 'message'}),   // placeholder object
                headers: {
                    'Content-type': 'application,json'
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.msg_status);
                });
            // insert server route here to call twilio api
            // use another ajax call here to send a message to the server to send the message
            // in the server route, call the twilio code
            // TAKE THIS OUT: alert(`Here is the result: ${result.fname}`)
        });
        resultsContainer.appendChild(resultElement);
    });
};


// define callback function for event listener here or before the first function
    // ex: messageBtn.addEventListener('click', (event) => {}) (add to line 29)

// create a button to send message
// use ajax to send the message
// button should be displayed in the profile card
// event listener handles button click to send message
// do ajax call inside event listener
// server will take info about coach's phone number

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
            displayResults(data);
        });
});