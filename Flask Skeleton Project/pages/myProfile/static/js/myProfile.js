/*function EditFunction(){
  document.getElementById("Edit").disabled = true;
  document.getElementById("fname").disabled = false;
  document.getElementById("lname").disabled = false;
  document.getElementById("Email").disabled = false;
  document.getElementById("Uname").disabled = false;
  document.getElementById("Gender").disabled = false;
  document.getElementById("Academic").disabled = false;
  document.getElementById("City").disabled = false;
  document.getElementById("AboutMe").disabled = false;
  document.getElementById("FinishEdit").disabled = false;
}

function FinishEdit() {
  document.getElementById("Edit").disabled = false;
  document.getElementById("fname").disabled = true;
  document.getElementById("lname").disabled = true;
  document.getElementById("Email").disabled = true;
  document.getElementById("Uname").disabled = true;
  document.getElementById("Gender").disabled = true;
  document.getElementById("Academic").disabled = true;
  document.getElementById("City").disabled = true;
  document.getElementById("AboutMe").disabled = true;
  document.getElementById("FinishEdit").disabled = true;
}*/
function EditFunction(){
  document.getElementById('changeMyDetails').style.display='block';
}


function ClickFunctionClose() {
    document.getElementById('changeMyDetails').style.display = 'none';
}

// Get the modal
var Details = document.getElementById('changeMyDetails');

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == Details) {
          Details.style.display = "none";
      }
}