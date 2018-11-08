function get_destino(){
  var tipo = document.getElementById("tipo_des");
  if (tipo.value == 1){
    document.getElementById("dest_anuncios").style.display = 'block';
    document.getElementById("dest_gravacoes").style.display = 'none';
    document.getElementById("dest_numeros").style.display = 'none';
    document.getElementById("dest_uras").style.display = 'none';
    document.getElementById("dest_filas").style.display = 'none';
    document.getElementById("dest_chamadasGrupo").style.display = 'none';
    document.getElementById("dest_condicoes").style.display = 'none';
    document.getElementById("dest_troncos").style.display = 'none';
  }else{
    if (tipo.value == 2){
      document.getElementById("dest_anuncios").style.display = 'none';
      document.getElementById("dest_gravacoes").style.display = 'block';
      document.getElementById("dest_numeros").style.display = 'none';
      document.getElementById("dest_uras").style.display = 'none';
      document.getElementById("dest_filas").style.display = 'none';
      document.getElementById("dest_chamadasGrupo").style.display = 'none';
      document.getElementById("dest_condicoes").style.display = 'none';
      document.getElementById("dest_troncos").style.display = 'none';
    }else{
      if (tipo.value == 3){
        document.getElementById("dest_anuncios").style.display = 'none';
        document.getElementById("dest_gravacoes").style.display = 'none';
        document.getElementById("dest_numeros").style.display = 'block';
        document.getElementById("dest_uras").style.display = 'none';
        document.getElementById("dest_filas").style.display = 'none';
        document.getElementById("dest_chamadasGrupo").style.display = 'none';
        document.getElementById("dest_condicoes").style.display = 'none';
        document.getElementById("dest_troncos").style.display = 'none';
      }else{
        if (tipo.value == 4){
          document.getElementById("dest_anuncios").style.display = 'none';
          document.getElementById("dest_gravacoes").style.display = 'none';
          document.getElementById("dest_numeros").style.display = 'none';
          document.getElementById("dest_uras").style.display = 'block';
          document.getElementById("dest_filas").style.display = 'none';
          document.getElementById("dest_chamadasGrupo").style.display = 'none';
          document.getElementById("dest_condicoes").style.display = 'none';
          document.getElementById("dest_troncos").style.display = 'none';
        }else{
          if (tipo.value == 5){
            document.getElementById("dest_anuncios").style.display = 'none';
            document.getElementById("dest_gravacoes").style.display = 'none';
            document.getElementById("dest_numeros").style.display = 'none';
            document.getElementById("dest_uras").style.display = 'none';
            document.getElementById("dest_filas").style.display = 'block';
            document.getElementById("dest_chamadasGrupo").style.display = 'none';
            document.getElementById("dest_condicoes").style.display = 'none';
            document.getElementById("dest_troncos").style.display = 'none';
          }else{
            if (tipo.value == 6){
              document.getElementById("dest_anuncios").style.display = 'none';
              document.getElementById("dest_gravacoes").style.display = 'none';
              document.getElementById("dest_numeros").style.display = 'none';
              document.getElementById("dest_uras").style.display = 'none';
              document.getElementById("dest_filas").style.display = 'none';
              document.getElementById("dest_chamadasGrupo").style.display = 'block';
              document.getElementById("dest_condicoes").style.display = 'none';
              document.getElementById("dest_troncos").style.display = 'none';
            }else{
              if (tipo.value == 7){
                document.getElementById("dest_anuncios").style.display = 'none';
                document.getElementById("dest_gravacoes").style.display = 'none';
                document.getElementById("dest_numeros").style.display = 'none';
                document.getElementById("dest_uras").style.display = 'none';
                document.getElementById("dest_filas").style.display = 'none';
                document.getElementById("dest_chamadasGrupo").style.display = 'none';
                document.getElementById("dest_condicoes").style.display = 'block';
                document.getElementById("dest_troncos").style.display = 'none';
              }else{
                if (tipo.value == 8){
                  document.getElementById("dest_anuncios").style.display = 'none';
                  document.getElementById("dest_gravacoes").style.display = 'none';
                  document.getElementById("dest_numeros").style.display = 'none';
                  document.getElementById("dest_uras").style.display = 'none';
                  document.getElementById("dest_filas").style.display = 'none';
                  document.getElementById("dest_chamadasGrupo").style.display = 'none';
                  document.getElementById("dest_condicoes").style.display = 'none';
                  document.getElementById("dest_troncos").style.display = 'block';
                }else{
                  document.getElementById("dest_anuncios").style.display = 'none';
                  document.getElementById("dest_gravacoes").style.display = 'none';
                  document.getElementById("dest_numeros").style.display = 'none';
                  document.getElementById("dest_uras").style.display = 'none';
                  document.getElementById("dest_filas").style.display = 'none';
                  document.getElementById("dest_chamadasGrupo").style.display = 'none';
                  document.getElementById("dest_condicoes").style.display = 'none';
                  document.getElementById("dest_troncos").style.display = 'none';
                }
            }
          }
        }
      }
    }
  }
  }
}
