function init() {
    d3.json('https://ufcmatchdata.herokuapp.com/combined').then(data => {
        var combined_data = JSON.parse(data)
        console.log('top data')
        console.log(combined_data)
    });
}

init();