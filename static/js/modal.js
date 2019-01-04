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

function mostraDet(id){
  $.ajax({
     url: '/relatorios/detalhes/',
     cache: false,
     type: "GET",
     data: {
          'id': id
        },
     dataType: 'json',
     success: function(dados){
       var chamada = JSON.parse(dados);
       console.log(chamada);

       var modal = document.getElementById('myModal');
       var table = "";
       var recordingfile = chamada['recordingfile']
       if (recordingfile !=null){
         var string = recordingfile.substring(0, 34);
         if(string == "/media/var/spool/asterisk/monitor/"){
           aux = recordingfile.split("/media/var/spool/asterisk/monitor/");
           recordingfile = "/media/" +aux[1];
         }
       }
         table= "<table>"
         +"<tr><td>Data:</td><td>"+chamada['calldate']+"</td></tr>"
         +"<tr><td>Clid:</td><td>"+chamada['clid']+"</td></tr>"
         +"<tr><td>Origem:</td><td>"+chamada['src']+"</td></tr>"
         +"<tr><td>Destino:</td><td>"+chamada['dst']+"</td></tr>"
         +"<tr><td>Dcontext:</td><td>"+chamada['dcontext']+"</td></tr>"
         +"<tr><td>Canal de origem:</td><td>"+chamada['channel']+"</td></tr>"
         +"<tr><td>Canal de destino:</td><td>"+chamada['dstchannel']+"</td></tr>"
         +"<tr><td>Lastapp:</td><td>"+chamada['lastapp']+"</td></tr>"
         +"<tr><td>Lastdata:</td><td>"+chamada['lastdata']+"</td></tr>"
         +"<tr><td>Duração:</td><td>"+chamada['duration']+"</td></tr>"
         +"<tr><td>Billsec:</td><td>"+chamada['billsec']+"</td></tr>"
         +"<tr><td>Status:</td><td>"+chamada['disposition']+"</td></tr>"
         +"<tr><td>Amaflags:</td><td>"+chamada['amaflags']+"</td></tr>"
         +"<tr><td>Accountcode:</td><td>"+chamada['accountcode']+"</td></tr>"
         +"<tr><td>Userfield:</td><td>"+chamada['userfield']+"</td></tr>"
         +"<tr><td>Cnum:</td><td>"+chamada['cnum']+"</td></tr>"
         +"<tr><td>Cnam:</td><td>"+chamada['cnam']+"</td></tr>"
         +"<tr><td>Outbound_cnum:</td><td>"+chamada['outbound_cnum']+"</td></tr>"
         +"<tr><td>Outbound_cnam:</td><td>"+chamada['outbound_cnam']+"</td></tr>"
         +"<tr><td>Dst_cnam:</td><td>"+chamada['dst_cnam']+"</td></tr>"
         +"<tr><td>Did:</td><td>"+chamada['did']+"</td></tr>";

         if (recordingfile !=null){
           table = table +'<tr><td>Gravação:</td><td><audio controls><source src="'+recordingfile+'" type="audio/wav"></audio></td></tr>';
         }else{
           table = table +"<tr><td>Sem gravação cadastrada</td><td></td></tr>";
         }

         if (chamada['tamVar']>0){
           table= table + "<tr><td><strong>Variáveis</strong></td><td></td></tr>";
         }
         for( var i =0; i<chamada['tamVar']; i++){
           table= table + "<tr><td>Variável:</td><td>"+chamada['var'+i]+"</td></tr>"
           + "<tr><td>Valor:</td><td>"+chamada['valor'+i]+"</td></tr>";
         }

        table = table +"</table>";



       var newTextBoxDiv = $('</fieldset>');
       newTextBoxDiv.html(chamada['calldate']);
       newTextBoxDiv.appendTo("#detahesModal");
       $('#detahesModal').append(table);


       modal.style.display = "block";

     }
   });
 }
