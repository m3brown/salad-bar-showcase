var selectedToppings = 0;

function refreshCounter() {
  $('#counter').text(selectedToppings);
}

function addToSelected() {
    $(this).off('click').on('click', removeFromSelected);
    $('#toppingsSelected').append($(this));
    selectedToppings++;
    refreshCounter();
}

function removeFromSelected() {
    $(this).off('click').on('click', addToSelected);
    $('#toppingsChoices').append($(this));
    selectedToppings--;
    refreshCounter();
}

function hoverInfo() {
    $(".ingredientInfo").load('/'+$(this).attr("id")+'/');
}

function noHoverInfo() {
    $(".ingredientInfo").html('');
}

$(document).ready(function() {
  $( refreshCounter );
  $( "#toppingsChoices .topping" ).click(addToSelected);
  $( "#toppingsChoices .topping" ).hover(hoverInfo, noHoverInfo);
});

