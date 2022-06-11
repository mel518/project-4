
function init() {
  d3.json("https://ufcmatchdata.herokuapp.com/fighters").then(data => {

    // Drop down menu creation
    let dropdownMenu = d3.select("#selDataset");
    data.forEach((uniqueVarietyList) => {
      dropdownMenu.append('option').text(uniqueVarietyList)
    })
    //this is works because of Closure and Scope (Unique)
    // Start at wine option 0
    var result = data[0];

    // // for (let i = 0; i<data.length; i++){
    // // console.log(data.country);
    buildMetadata(result)
    //   var result = data[0].variety;
    // winelist(wineVariety);
  });
  
}

// New Option for Drop Down, re-load all info


// Initialize the code
init();


function init1() {
  d3.json("https://ufcmatchdata.herokuapp.com/fighters").then(data => {

    // Drop down menu creation
    let dropdownMenu = d3.select("#selDataset1");
    data.forEach((uniqueVarietyList) => {
      dropdownMenu.append('option').text(uniqueVarietyList)
    })
    //this is works because of Closure and Scope (Unique)
    // Start at wine option 0
    var result = data[0];

    // // for (let i = 0; i<data.length; i++){
    // // console.log(data.country);
    buildMetadata(result)
    //   var result = data[0].variety;
    // winelist(wineVariety);
  });
  
}

// New Option for Drop Down, re-load all info


// Initialize the code
init1();
//

