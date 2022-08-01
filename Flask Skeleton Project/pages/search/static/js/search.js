function ViewSearch() {
    const dateInput = document.getElementById("PickDate");
    if (!dateInput.value || !PickTimeRange1.value || !PickTimeRange2.value) {
        document.getElementById("BadInput").style.display = "block";
        document.getElementById("containerWorkoutsSearch").style.display = "none";
    } else {
        document.getElementById("containerWorkoutsSearch").style.display = "block";
        document.getElementById("BadInput").style.display = "none";
    }


}
function ClickSearchTable(){
  document.getElementById('openSearchTable').style.display='block';
}

function ClickFunctionCloseSearchTable(){
  document.getElementById('openSearchTable').style.display='none';
}


var modal = document.getElementById('openSearchTable');
  // When the user clicks anywhere outside of the modalTable, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
}

function TDate() {
    var UserDate = document.getElementById("PickDate").value;
    var ToDate = new Date();

    if (new Date(UserDate).getTime() <= ToDate.getTime()) {
          alert("The Date must be Bigger or Equal to today date");
          return false;
     }
    return true;
}
