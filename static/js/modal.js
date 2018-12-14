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
  var table = "";
  if (recordingfile != ""){
    table= "<table>"
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
    +"<tr><td>Billsec:</td><td>"+billsec+"</td></tr>"
    +"<tr><td>Status:</td><td>"+disposition+"</td></tr>"
    +"<tr><td>Amaflags:</td><td>"+amaflags+"</td></tr>"
    +"<tr><td>Accountcode:</td><td>"+accountcode+"</td></tr>"
    +"<tr><td>Userfield:</td><td>"+userfield+"</td></tr>"
    +"<tr><td>Cnum:</td><td>"+cnum+"</td></tr>"
    +"<tr><td>Cnam:</td><td>"+cnam+"</td></tr>"
    +"<tr><td>Outbound_cnum:</td><td>"+outbound_cnum+"</td></tr>"
    +"<tr><td>Outbound_cnam:</td><td>"+outbound_cnam+"</td></tr>"
    +"<tr><td>Dst_cnam:</td><td>"+dst_cnam+"</td></tr>"
    +"<tr><td>Did:</td><td>"+did+"</td></tr>"
    +'<tr><td>Gravação:</td><td><audio controls><source src="'+recordingfile+'" type="audio/wav"></audio></td></tr>'
    +"</table>";
  }else{
    table= "<table>"
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
    +"<tr><td>Billsec:</td><td>"+billsec+"</td></tr>"
    +"<tr><td>Status:</td><td>"+disposition+"</td></tr>"
    +"<tr><td>Amaflags:</td><td>"+amaflags+"</td></tr>"
    +"<tr><td>Accountcode:</td><td>"+accountcode+"</td></tr>"
    +"<tr><td>Userfield:</td><td>"+userfield+"</td></tr>"
    +"<tr><td>Cnum:</td><td>"+cnum+"</td></tr>"
    +"<tr><td>Cnam:</td><td>"+cnam+"</td></tr>"
    +"<tr><td>Outbound_cnum:</td><td>"+outbound_cnum+"</td></tr>"
    +"<tr><td>Outbound_cnam:</td><td>"+outbound_cnam+"</td></tr>"
    +"<tr><td>Dst_cnam:</td><td>"+dst_cnam+"</td></tr>"
    +"<tr><td>Did:</td><td>"+did+"</td></tr>"
    +"<tr><td>Recordingfile:</td><td>"+recordingfile+"</td></tr>"
    +"</table>";
  }

  var newTextBoxDiv = $('</fieldset>');
  newTextBoxDiv.html(calldate);
  newTextBoxDiv.appendTo("#detahesModal");
  $('#detahesModal').append(table);


  modal.style.display = "block";
}
