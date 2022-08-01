function ClickFunctionLogIn(){
  document.getElementById('id01').style.display='block';
}
function ClickFunctionPass(){
  document.getElementById('id02').style.display='block';
}
function ClickFunctionCloseNone(){
  document.getElementById('id01').style.display='none';
}

function ClickFunctionCloseNonePass(){
  document.getElementById('id02').style.display='none';
}


// Get the modal
var modal = document.getElementById('id01');

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
}