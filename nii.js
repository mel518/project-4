// function scatterpoints(sample){
  d3.json('https://ufcmatchdata.herokuapp.com/combined').then(async data => {
    var combined_data = JSON.parse(data)
    console.log(combined_data[1].avg_BODY_att);
    console.log('nii')
    
       
  
        let KD= [];
        let total_strike= [];
        let winename= [];
  
        for(var i = 0; i<combined_data.length; i++) {
          combined_data[i].Referee
          KD.push(combined_data[i].Referee);
        }
        console.log(KD);
  
        // for(var i = 0; i<combined_data.length; i++) {
        //   combined_data[i].avg_KD
        //   total_strike.push(resultArray[i].avg_KD);
        // }
  
        // for(var i = 0; i<resultArray.length; i++) {
        //   resultArray[i].price
        //   winename.push(resultArray[i].title);
        // }
        
      //   console.log(winename);
  
  
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
  // }

  // scatterpoints();