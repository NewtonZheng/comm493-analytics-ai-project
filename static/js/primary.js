//primary.js

//When user clicks on the submit button, the following code will run
$("#output1").on("click", function(event){

  //Prevents default html form submission from happening
  event.preventDefault();

  //Takes the input from the user from the input and store in a variable
  //var user_input = ;

  //return false if user input is null
  if (user_input.length <= 0) return false;

  //Check that comment is there, and if so then send an AJAX request
  //Python will have to check the parameter probably

  $.ajax({
    url: '/search', //Set endpoint URL to display results as @ /search
    method: 'POST',
    data: {
      exam : $("#exam_selection").val(),
      group : $("course_selection").val(),
 //stores user input as a 'text' parameter data
}
    beforeSend: function(){
      //Run this function before the request is sent to the Python Code

      //Optional loader can be included
      //$("#loader").fadeIn();
    }
    success: function(response){
      //Following code is triggered when response is returned from the Python code
      //So here we decide the way that we show our responses
      $("#final_results").html("<p>The following courses match your results" + (response.$("#course_results")]) + "</p>");


      //alert(response);

      //Optional loader can be included
      //$("#loader").fadeOut();
    }

  })
