$(document).ready(function(){
  var modal = document.getElementById('myModal');
  var span = document.getElementsByClassName("close")[0];
var fieldset = document.getElementById('detahesModal');
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    fieldset.innerHTML="";
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      fieldset.innerHTML="";
      modal.style.display = "none";
    }
  }
});


function mostraDetalhes(calldate, clid, src , dst, dcontext, channel, dstchannel, lastapp, lastdata,duration, billsec ,disposition, amaflags, accountcode, userfield, recordingfile, cnum, cnam, outbound_cnum, outbound_cnam, dst_cnam, did){
  var modal = document.getElementById('myModal');

  var table= "<table>"
  +"<tr><td>Data:</td><td>"+calldate+"</td></tr>"
  +"<tr><td>Clid:</td><td>"+clid+"</td></tr>"
  +"<tr><td>Origem:</td><td>"+src+"</td></tr>"
  +"<tr><td>Destino:</td><td>"+dst+"</td></tr>"
  +"<tr><td>Dcontext:</td><td>"+dcontext+"</td></tr>"
  +"<tr><td>Canal de origem:</td><td>"+channel+"</td></tr>"
  +"<tr><td>Canal de destino:</td><td>"+dstchannel+"</td></tr>"
  +"<tr><td>Lastapp:</td><td>"+lastapp+"</td></tr>"
  +"<tr><td>Lastdata:</td><td>"+lastdata+"</td></tr>"
  +"<tr><td>Duração:</td><td>"+duration+"</td></tr>"
  +"<tr><td>billsec:</td><td>"+billsec+"</td></tr>"
  +"<tr><td>Status:</td><td>"+disposition+"</td></tr>"
  +"<tr><td>amaflags:</td><td>"+amaflags+"</td></tr>"
  +"<tr><td>accountcode:</td><td>"+accountcode+"</td></tr>"
  +"<tr><td>userfield:</td><td>"+userfield+"</td></tr>"
  +"<tr><td>recordingfile:</td><td>"+recordingfile+"</td></tr>"
  +"<tr><td>cnum:</td><td>"+cnum+"</td></tr>"
  +"<tr><td>cnam:</td><td>"+cnam+"</td></tr>"
  +"<tr><td>outbound_cnum:</td><td>"+outbound_cnum+"</td></tr>"
  +"<tr><td>outbound_cnam:</td><td>"+outbound_cnam+"</td></tr>"
  +"<tr><td>dst_cnam:</td><td>"+dst_cnam+"</td></tr>"
  +"<tr><td>did:</td><td>"+did+"</td></tr>"
  +"</table>";

  var newTextBoxDiv = $('</fieldset>');
  newTextBoxDiv.html(calldate);
  newTextBoxDiv.appendTo("#detahesModal");
  $('#detahesModal').append(table);


  modal.style.display = "block";
}
