function spline_chart() {
  return new Highcharts.Chart({
    chart: {
      borderWidth: 0,
      backgroundColor: null,
      renderTo: 'right_chart',
      defaultSeriesType: 'spline',
    },
    exporting: {
      enabled: false
    },
    credits: {
      enabled: false
    },
    tooltip: {
      enabled: false
    },
    title: {
    text: 'Bandwidth',
    style: {
        color: 'transparent',
        fontSize:'50px'
    },
    },
    legend: {
      enabled: false,
      itemStyle: {
        font: 'Roboto Condensed, sans-serif',
        color: '#0077C8'
      },
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      floating: true,
    },
    xAxis: {
      title: {
        text: 'Test',
        style: {
            color: 'transparent',
            fontSize:'20px'
        }
      },
      labels: {
        enabled: false
      },
      minorTickLength: 0,
      tickLength: 0,
      lineWidth: 0,
      minorGridLineWidth: 0,
      lineColor: 'transparent'
    },
    yAxis: {
      min: 0,
      max: 18,
      title: {
        text: '',
        margin: 0,
        style: {
          font: 'Roboto Condensed, sans-serif',
          color: '#0077C8'
        }

      },
      labels: {
        formatter: function() {
          val = this.value;
          return '' + val.toLocaleString() + '';
        },
        style: {
          color: '#0077C8;',
          fontSize: '16px'
        },
      },
      minorTickLength: 0,
      tickLength: 0,
      lineWidth: 0,
      minorGridLineWidth: 0,
      lineColor: 'transparent'
    },
    plotOptions: {
      areaspline: {
        fillOpacity: 0.75,
        lineWidth: 10,
        marker: {
          enabled: false
        }
      },
      spline: {
        lineWidth: 7,
        marker: {
          enabled: false
        }
      },
      series: {
        marker: {
          states: {
            hover: {
              enabled: false
            }
          }
        }
      }
    },
    series: [{
      name: 'test',
      data: [],
      color: '#0077C8',
    }]
  });
}