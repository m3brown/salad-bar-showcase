var selectedToppings = 0;

function refreshCounter() {
  $('#counter').text(selectedToppings);
}

function addToSelected(topping) {
    $(this).off('click').on('click', removeFromSelected);
    $('#toppingsSelected').append($(this));
    selectedToppings++;
    refreshCounter();
}

function removeFromSelected(topiing) {
    $(this).off('click').on('click', addToSelected);
    $('#toppingsChoices').append($(this));
    selectedToppings--;
    refreshCounter();
}

$(document).ready(function() {
  $( refreshCounter );
  $( "#toppingsChoices .topping" ).click(addToSelected);
});

