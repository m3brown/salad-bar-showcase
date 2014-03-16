var cost_data;
var chart;
var options_cost;
var calorie_data;
var chartCalories;
var options_calories;

google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(initializeCharts);

function initializeCharts(){
  chartCost = new google.visualization.ColumnChart(document.getElementById('cost_chart'));
  chartCalories = new google.visualization.ColumnChart(document.getElementById('calorie_chart'));

  cost_data = new google.visualization.arrayToDataTable([
    ['Category', 'Cost'],
    ['Cost', 0.00]
  ]);

  calorie_data = google.visualization.arrayToDataTable([
    ['Category', 'Calories'],
    ['Calories', 0]
  ]);

  options_cost = {
    width: 100,
    legend: {position: "none"},
    bar: {groupWidth: "25%"},
    vAxis: {minValue: 0.00, maxValue: 10.00, format: "$##.00"},
    chartArea: {left: "50"},
    animation: {duration: 500, easing: 'out'}
  };

  options_calories = {
    width: 100,
    legend: {position: "none"},
    bar: {groupWidth: "25%"},
    vAxis: {minValue: 0.00, maxValue: 1000},
    chartArea: {left: "50"},
    animation: {duration: 500, easing: 'out'},
  };

  
  drawCharts();
}

function drawCharts() {
  chartCost.draw(cost_data, options_cost);
  chartCalories.draw(calorie_data, options_calories);
}