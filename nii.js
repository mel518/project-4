// 'https://ufcmatchdata.herokuapp.com/recent_matches'
// 'https://ufcmatchdata.herokuapp.com/combined/${fighter}'
function visuals(sample){
  d3.json('https://ufcmatchdata.herokuapp.com/recent_matches').then(async data => {
    var combined_data = JSON.parse(data)
    console.log(combined_data[1].avg_BODY_att);
    console.log('nii')
    
       
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
  
        
  
      //   var data = [
      //     {
      //       x: winepoints,
      //       y: wineprice.length,
      //       type: 'histogram',
      //     marker: {
      //       color: '#C70039',
      //       line: {
      //         color:  "rgba(255, 100, 102, 1)",
      //         width: 1
      //       }
      //     },
      //     }
      //   ];
      //   let barLayout= {
      //     title: 'Histogram of Wine Rating',
      //     margin: {t:0},
      //     hovermode: "closest",
      //     xaxis: {title: 'Wine Ratings'},
      //     yaxis: {title:'# of wines'},
      //     margin: {t:30}
      //   };
      //   Plotly.newPlot('bar', data,barLayout);
  
  
    });
  }


  // function optionChanged(sample) {
  //   console.log(sample);
  //   init(sample);
  //   init1(sample);
  //   
  // }

  visuals();