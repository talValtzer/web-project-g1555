var mysql = require('mysql');

function JoinWorkout(){
document.getElementById("JoinBtn").innerHTML = " ";
//document.getElementById("JoinBtn").hidden = true;
//document.getElementById("Unsubscribe").hidden = false;
}

let parTable= document.getElementById("work_Participants");

function deleteMyself(){
  //document.getElementById("JoinBtn").hidden = false;
 // document.getElementById("Unsubscribe").hidden = true;
  document.getElementById("work_Participants").deleteRow(document.getElementById("work_Participants").rows.length-1);
}