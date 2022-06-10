function init(sample) {
    d3.json(`http://127.0.0.1:5000/select/${sample}`).then(data => {
        console.log('top data')
        console.log(data)

    let result = data;
    console.log(result)

    let meta = [];
    fighters = JSON.parse(result);
    console.log(fighters)

    let displayinfo = d3.select('#selDataset');
    displayinfo.html('');
    fighters.forEach(k => {
        console.log(k)
        displayinfo.append('option').text(k[0] + ':' + k[1]).append('br')
    });





    // if () {
    //     let displayinfo = d3.select('#sample-metadata2');
    //     displayinfo.html('');
    //     Object.entries(meta[0]).forEach(k => {
    //         console.log(k)
    //         displayinfo.append('panel-body').text(k[0].toUpperCase() + ': ' + k[1]).append('br');
    //     });
    //     //display the second top option
    //     let displayinfo2 = d3.select('#sample-metadata3');
    //     displayinfo2.html('');
    //     Object.entries(meta[1]).forEach(k2 => {
    //         console.log(k2)
    //         displayinfo2.append('panel-body').text(k2[0].toUpperCase() + ':' + k2[1]).append('br');
    //     });
    // }




    });

}

init();