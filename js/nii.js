// 'https://ufcmatchdata.herokuapp.com/recent_matches'
// 'https://ufcmatchdata.herokuapp.com/combined/${fighter}'




function visuals(fighter){
 
  console.log('fighter' , fighter)
  d3.json(`http://127.0.0.1:5000/combined/${fighter}`).then( data => {
    
    let combined_data=data;
    console.log(data);
    console.log()
    
        
        let dte= [];
        let KD= [];
        let total_strike= [];
        let total_strike_lnd= [];
  
        for(var i = 0; i<combined_data.length; i++) {
          combined_data[i].avg_KD
          KD.push(combined_data[i].avg_KD);
        }
        console.log(KD);
  
        for(var i = 0; i<combined_data.length; i++) {
          combined_data[i].avg_TOTAL_STatt
          total_strike.push(combined_data[i].avg_TOTAL_STatt);
        }
  
        for(var i = 0; i<combined_data.length; i++) {
          combined_data[i].date
          dte.push(combined_data[i].date);
        }
        
        for(var i = 0; i<combined_data.length; i++) {
          combined_data[i].avg_TOTAL_STlanded
          total_strike_lnd.push(combined_data[i].avg_TOTAL_STlanded);
        }
         console.log(total_strike);
  
  
      //   let trace2 = {
      //     x: (winepoints),
      //     y: (wineprice),
      //     //text: (otu_labelss),
      //     text: [winename],
      //     mode: 'markers',
      //     marker: {
      //     color: (winepoints),
      //     size: (15),
      //     colorscale: 'Fire'
          
      //   }
      // };
      
      // let bubbleLayout= {
      //     title: 'Variety Price by Ratings',
      //     margin: {t:0},
      //     hovermode: "closest",
      //     xaxis: {title: 'Wine Ratings'},
      //     yaxis: {title:'Wine Prices'},
      //     margin: {t:30}
      // };
  
      // let data2=[trace2]
      // Plotly.newPlot('bubble', data2, bubbleLayout);
  
        
  
        var data = [
          {
            x: dte,
            y: KD,
            type: 'histogram',
            marker: {
              color: '#3a485e',
              line: {
                color:  "rgba(251, 251, 251, 0.15)",
                width: 1
              }
            },
            }
        ];
        let barLayout= {
          title: 'KD History',
          margin: {t:0},
          hovermode: "closest",
          xaxis: {title: 'Date'},
          yaxis: {title:'KD'},
          margin: {t:30}
        };
        Plotly.newPlot('bar', data,barLayout);
  
  
    });
  }

  function visuals2(fighterr){
    //const visuals = d3.select("#selDataset").node().value;
    console.log('fighter' , fighterr)
    d3.json(`http://127.0.0.1:5000/combined/${fighterr}`).then( data => {
      // var combined_data = JSON.parse(data)
      let combined_data=data;
      console.log(data);
      console.log()
      //playerwebsite = data.filter(player => player.fighters === visuals)[0]
          
          let dte= [];
          let KD= [];
          let total_strike= [];
          let total_strike_lnd= [];
    
          for(var i = 0; i<combined_data.length; i++) {
            combined_data[i].avg_KD
            KD.push(combined_data[i].avg_KD);
          }
          console.log(KD);
    
          for(var i = 0; i<combined_data.length; i++) {
            combined_data[i].avg_TOTAL_STatt
            total_strike.push(combined_data[i].avg_TOTAL_STatt);
          }
    
          for(var i = 0; i<combined_data.length; i++) {
            combined_data[i].date
            dte.push(combined_data[i].date);
          }
          
          for(var i = 0; i<combined_data.length; i++) {
            combined_data[i].avg_TOTAL_STlanded
            total_strike_lnd.push(combined_data[i].avg_TOTAL_STlanded);
          }
           console.log(total_strike);
    
    
        //   let trace2 = {
        //     x: (winepoints),
        //     y: (wineprice),
        //     //text: (otu_labelss),
        //     text: [winename],
        //     mode: 'markers',
        //     marker: {
        //     color: (winepoints),
        //     size: (15),
        //     colorscale: 'Fire'
            
        //   }
        // };
        
        // let bubbleLayout= {
        //     title: 'Variety Price by Ratings',
        //     margin: {t:0},
        //     hovermode: "closest",
        //     xaxis: {title: 'Wine Ratings'},
        //     yaxis: {title:'Wine Prices'},
        //     margin: {t:30}
        // };
    
        // let data2=[trace2]
        // Plotly.newPlot('bubble', data2, bubbleLayout);
    
          
    
          var data = [
            {
              x: dte,
              y: KD,
              type: 'histogram',
            marker: {
              color: '#3a485e',
              line: {
                color:  "rgba(251, 251, 251, 0.15)",
                width: 1
              }
            },
            }
          ];
          let barLayout= {
            title: 'KD History',
            margin: {t:0},
            hovermode: "closest",
            xaxis: {title: 'Date'},
            yaxis: {title:'KD'},
            margin: {t:30}
          };
          Plotly.newPlot('bubble', data,barLayout);
    
    
      });
    }

  

 visuals();
 visuals2();