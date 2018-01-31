Highcharts.chart('left_chart', {
  chart: {
    type: 'column',
    borderWidth: 0,
    backgroundColor: 'transparent',
  },
  title: {
    text: 'Bandwidth',
    style: {
        color: ' #0077C8',
        fontSize:'50px'
    },
    align: 'left',
//    x: 70,
  },
  xAxis: {
    categories: ['SSD', 'NVME', 'NVDIMM'],
//    lineWidth: 0,
//    minorGridLineWidth: 0,
//    lineColor: 'transparent',
//    minorTickLength: 0,
//    tickLength: 0,
//    gridLineColor: 'transparent',
    labels: {
        style: {
            color: ' #0077C8',
            fontSize:'20px'
        }
    }
  },
  yAxis: {
    min: 0,
    max: 20,
    title: {
      text: '',
      style: {
            color: ' #0077C8',
            fontSize:'20px'
       },
    },
    lineWidth: 0,
    minorGridLineWidth: 0,
    lineColor: 'transparent',
    minorTickLength: 0,
    tickLength: 0,
    gridLineColor: 'transparent',
    labels: {
        style: {
            color: ' #0077C8',
            fontSize:'15px'
        }
    }
  },
  legend: {
    enabled: false
  },
  credits: {
    enabled: false
  },
  exporting: {
    enabled: false
  },
  tooltip: {
    enabled: false
  },
  plotOptions: {
    series: {
      stacking: 'normal',
      borderRadius: 5
    }
  },
  annotations: [{
  labelOptions: {
            shape: 'circle',
            align: 'center',
            y: -10,
            justify: false,
            crop: false,
            shadow: true,
            padding: 12,
            borderWidth: 3,
            borderColor: '#0077C8',
            style: {
                fontSize: '20px',
                textOutline: '1px white'
            }
    },
    labels: [{
        point: {
            x: 0,
            y: 7.5,
            xAxis: 0,
            yAxis: 0
        },
        backgroundColor: "white",
        text: 'Price You Want',
        style: {
            color: '#2C2C2E',
        }
    },{
        point: {
            x: 2,
            y: 15.25,
            xAxis: 0,
            yAxis: 0
        },
        backgroundColor: "white",
        text: 'Performance You Want',
        style: {
            color: '#2C2C2E',
        }
    }]
  }],
  series: [{
    name: 'Line',
    data: [1, 1, 1],
    color: '#58595B',
    borderColor: '#2C2C2E'

  },{
    name: 'Blank',
    data: [.5, .5, .5],
    color: 'transparent',
    borderColor: 'transparent'

  },{
    name: 'Bar',
    data: [6, 9, 14],
    color: 'transparent',
    borderColor: 'transparent',
  }]
});