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
    
    // Start at fighter option 0
    var result = data[0];
    
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
    // visuals(fighter1)
    // window.open(data[0].webpage, "_blank");
  })
}
// New Option for Drop Down, re-load all info
function fighter2() {

  const fighter2 = d3.select("#selDataset1").node().value;

  d3.json(`http://127.0.0.1:5000//ufc`).then(data => {
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


function optionChanged(fighter) {
  init(fighter);
  visuals(fighter);
  visuals3(fighter);
 
}

function optionsChanged(fighterr) {
  init(fighterr);
  visuals2(fighterr);
  visuals4(fighterr);
}

// Initialize the code
init();