const displayResults = (searchResults) => {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = "";

    searchResults.forEach((result) => {
        resultElement = document.createElement('div');
        resultElement.innerHTML = (
            `Student: ${result.fname} ${result.lname}<br>`
            + `Gender: ${result.gender}<br>`
            + `Height: ${result.height} inches<br>`
            + `Weight: ${result.weight} pounds<br>`
            + `Sport: ${result.sport_name}<br>`
            + `Position: ${result.position_id}<br>`
            + `Location: ${result.location_id}<br>`
            + `Bio: ${result.bio}<br>`
            + `Email: <a href="mailto:${result.student_email}">${result.student_email}</a><br><br>`
        );
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