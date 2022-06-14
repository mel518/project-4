async function predict() {
  const fighter1_el = document.getElementById("selDataset")
  const fighter2_el = document.querySelector("#selDataset1")
  console.log(fighter2_el)
  const fighter1 = fighter1_el?.value
  const fighter2 = fighter2_el?.value
  

    const rawResponse = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fighter1,
        fighter2
    })
    });
    const content = await rawResponse.json();
  
    console.log(content);
    const results = document.getElementById("results")
    results.innerHTML = content.prediction
 
}

function init() {
  d3.json("http://127.0.0.1:5000/fighters").then(data => {
    // Drop down menu creation
    let dropdownMenu = d3.select("#selDataset");
    data.forEach((uniqueVarietyList) => {
      dropdownMenu.append('option').text(uniqueVarietyList)
    })
    let dropdownMenu2 = d3.select("#selDataset1");
    data.forEach((uniqueVarietyList) => {
      dropdownMenu2.append('option').text(uniqueVarietyList)
    })
    //this is works because of Closure and Scope (Unique)
    // Start at wine option 0
    var result = data[0];
    visuals(result)

    // // for (let i = 0; i<data.length; i++){
    // // console.log(data.country);
    //   var result = data[0].variety;
    // winelist(wineVariety);
  });

}

// New Option for Drop Down, re-load all info
function fighter1() {

  const fighter1 = d3.select("#selDataset").node().value;

  d3.json(`http://127.0.0.1:5000//ufc`).then(data => {
    data = JSON.parse(data)
    console.log(data)
    playerwebsite = data.filter(player => player.fighters === fighter1)[0]?.webpage
    if (playerwebsite) {
      window.open(playerwebsite, "_blank");
    } else {
      alert("fighter does not exist")
    }
    // add listner (this is in the html)
    // window.open(data[0].webpage, "_blank");
  })
}
// New Option for Drop Down, re-load all info
function fighter2() {

  const fighter2 = d3.select("#selDataset1").node().value;

  d3.json(`http://127.0.0.1:5000/ufc`).then(data => {
    data = JSON.parse(data)
    console.log(data)
    playerwebsite = data.filter(player => player.fighters === fighter2)[0]?.webpage
    if (playerwebsite) {
      window.open(playerwebsite, "_blank");
    } else {
      alert("fighter does not exist")
    }
  })
}
// Initialize the code
init();




