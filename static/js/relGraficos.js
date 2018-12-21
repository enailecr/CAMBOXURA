$(document).ready(function(){
  $("#dados").submit( function(e) {
   e.preventDefault();

   var formData = $("#dados").serializeArray();

   $.ajax({
    	url: '/relatorios/busca-grafico-porcent/',
    	cache: false,
    	type: "GET",
    	data: formData,
      dataType: 'json',
    	success: function(dados){        
        var dados = JSON.parse(dados);
        var data = new google.visualization.DataTable();
              data.addColumn('string', 'Topping');
              data.addColumn('number', 'Slices');
              data.addRows(dados['originados']);
        var options = {'title':'Chamadas originadas por canal',
                        'colors': ['7f0000','ff9999', 'fac9b8', 'e2d4b7','9c9583','a62639', 'db324d', 'f15946','faedca','e6eed6'],
                        'width':400,
                        'height':300};

        var chart = new google.visualization.PieChart(document.getElementById('chart1_div'));
        chart.draw(data, options);

        data = new google.visualization.DataTable();
              data.addColumn('string', 'Topping');
              data.addColumn('number', 'Slices');
              data.addRows(dados['destinados']);
        options = {'title':'Chamadas destinadas ao canal',
                        'colors': ['7f0000','ff9999', 'fac9b8', 'e2d4b7','9c9583','a62639', 'db324d', 'f15946','faedca','e6eed6'],
                        'width':400,
                        'height':300};

        chart = new google.visualization.PieChart(document.getElementById('chart2_div'));
        chart.draw(data, options);
    	}
    });
  });

});


function selecionaFiltroPizza(){
  var filtro = document.getElementById('filtro').value;
  if(filtro == "hora") {
    document.getElementById('hora').style.display = "block";
    document.getElementById('dia').style.display ="none";
    document.getElementById('data_inicio').style.display = "none";
    document.getElementById('data_fim').style.display = "none";
  }else{
    if(filtro == "dia") {
      document.getElementById('hora').style.display = "none";
      document.getElementById('dia').style.display ="block";
      document.getElementById('data_inicio').style.display = "none";
      document.getElementById('data_fim').style.display = "none";
    }else{
      if(filtro == "inter") {
        document.getElementById('hora').style.display = "none";
        document.getElementById('dia').style.display ="none";
        document.getElementById('data_inicio').style.display = "block";
        document.getElementById('data_fim').style.display = "block";
      }else{
        document.getElementById('hora').style.display = "none";
        document.getElementById('dia').style.display ="none";
        document.getElementById('data_inicio').style.display = "none";
        document.getElementById('data_fim').style.display = "none";
      }
    }
  }
}

function montaGraficoOriginadas(originados){
  var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows(originados);
  var options = {'title':'Chamadas originadas por canal',
                  'colors': ['7f0000','ff9999', 'fac9b8', 'e2d4b7','9c9583','a62639', 'db324d', 'f15946','faedca','e6eed6'],
                  'width':400,
                  'height':300};

  var chart = new google.visualization.PieChart(document.getElementById('chart1_div'));
  chart.draw(data, options);

}
