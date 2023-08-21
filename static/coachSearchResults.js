const displayResults = (searchResults) => {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = "";

    searchResults.forEach((result) => {
        resultElement = document.createElement('div');
        resultElement.classList.add('profile-card')
        messageBtn = document.createElement('button');
        messageBtn.innerText = 'Send SMS';
        resultElement.innerHTML = (
            `Student: ${result.fname} ${result.lname}<br>`
            + `Gender: ${result.gender}<br>`
            + `Height: ${result.height} inches<br>`
            + `Weight: ${result.weight} pounds<br>`
            + `Sport: ${result.sport_name}<br>`
            + `Position: ${result.position_id}<br>`
            + `Location: ${result.location_id}<br>`
            + `Bio: ${result.bio}<br>`
            + `Email: <a href="mailto:${result.student_email}">${result.student_email}</a><br>`
        );
        // messageBtn.setAttribute('name', result.student_email)
        resultElement.appendChild(messageBtn);
        messageBtn.addEventListener('click', (event) => {
            fetch('/send_student_sms', {
                method: 'POST',
                body: JSON.stringify({coachMsg: 'message'}),
                headers: {
                    'Content-type': 'application.json'
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.msg_status);
                });
        });
        resultsContainer.appendChild(resultElement);
    });
};


const searchBtn = document.querySelector('#search-btn');

searchBtn.addEventListener('click', (event) => {
    event.preventDefault();

    const formData = new FormData(document.getElementById('search-students'));

    const searchData = {};
    formData.forEach((value, key) => {
        searchData[key] = value;
    });

    console.log(searchData);

    fetch('/search/results/students', {
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