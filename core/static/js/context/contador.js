
function mostrarResultado(box,num_max,campospan){
  var contagem_carac = box.length;
  if (contagem_carac != 0){
    document.getElementById(campospan).innerHTML = contagem_carac + " caracteres digitados,";
    if (contagem_carac == 1){
      document.getElementById(campospan).innerHTML = contagem_carac + " caracter digitado,";
    }
    if (contagem_carac >= num_max){
      document.getElementById(campospan).innerHTML = "Limite de caracteres excedido! ";
    }
  }else{
    document.getElementById(campospan).innerHTML = "Ainda não temos nada digitado.";
  }
}

function contarCaracteres(box,valor,campospan){
	var conta = valor - box.length;
	document.getElementById(campospan).innerHTML = " Você ainda pode digitar " + conta + " caracteres.";
	if(box.length >= valor){
		document.getElementById(campospan).innerHTML = "Opss.., você não pode mais digitar.";
		document.getElementById("campo").value = document.getElementById("campo").value.substr(0,valor);
	}
}
