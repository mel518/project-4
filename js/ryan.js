function visuals3(fighter) {
    console.log('fighter', fighter)
    d3.json(`https://ufcmatchdata.herokuapp.com/fighter_stats/${fighter}`).then(data => {
        console.log('blue data')
        console.log(data)

    // display the data
    let displayinfo = d3.select('#sample-metadata');
    displayinfo.html('');

    data.forEach(buy => 
        Object.entries(buy).map((lable)=> `${lable}`).forEach(item => 
            displayinfo.append('panel-body').text(item).append('br')))
    
    });

}

function visuals4(fighterr) {
    console.log('fighter', fighterr)
    d3.json(`https://ufcmatchdata.herokuapp.com/fighter_stats/${fighterr}`).then(data => {
        console.log('red data')
        console.log(data)

    // display the data
    let displayinfo2 = d3.select('#sample-metadata3');
    displayinfo2.html('');

    data.forEach(buy => 
        Object.entries(buy).map((lable)=> `${lable}`).forEach(item => 
            displayinfo2.append('panel-body').text(item).append('br')))
    
    });

}

visuals3();