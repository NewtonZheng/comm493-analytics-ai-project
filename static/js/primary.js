//primary.js

//When user clicks on the submit button, the following code will run
$("#output1").on("click", function(){

  //Takes the input from the user from the input and store in a variable
  var user_input = $("#exam_selection").val();

  //return false if user input is null
  if (user_input.length <= 0) return false;

  //If user wants exams, then this function runs
  if (user_input == "Exam")
