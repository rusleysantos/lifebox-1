// Variaveis globais:
var map;
var layer;
var markers = [];

// Inicializando o mapa do OpenStreetMap:
function initmap() {
	
	map = new L.Map('map', getPositionOptions());

	var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	layer = new L.TileLayer(osmUrl);
	map.setView(new L.LatLng(-20.297618, -40.295777), 10);
	map.addLayer(layer);

	//Atualiza os marcadores a cada x milisegundos:
	setInterval(function () {
		$.when(getData()).done(function (viagens) {
			
			//remove todos marcadores existentes no mapa:
			markers.map(function(item){item.remove()});
			
			var caixas = viagens.map(function(item){
				return item.caixa;
			});
			
			atualizarListaCaixas(caixas);
			
			//cria os marcadores:
			criarMarcadores(viagens);
		});
	}, (1 * 1000));
}

// Busca os dados das viagens ativas no sistema;
function getData() {
	return $.ajax({
		type: "get",
		url: "/api/viagem-ativas/",
		cache: false,
		Accept: "application/json",
		contentType: "application/json",
		success: function (response) {
			return response;
		},
		error: function (response, status, error) {
			console.log("Não foi possivel coletar as viagens ativas no sistema. Entre em contato com o administrador do Sistema.");
		}
	});
}

// Função que cria e atualiza os marcadores:
function criarMarcadores(_viagens) {
	//Verifica se existem viagens:
	if (_viagens == null || _viagens.length == 0) return;
	
	$.each(_viagens, function (idx, viagem) {
		if (viagem.detalhes != null) {
			
			// Pega o ultimo detalhe (ultima localização):
			var ultimoDetalhe = viagem.detalhes[viagem.detalhes.length - 1];

			//Cria o icone do marcador com a cor informada no cadastro:
			var _icon = L.AwesomeMarkers.icon({
				icon: 'cube',
				prefix: 'ion',
				markerColor: 'white',//valores possiveis: 'red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'
				iconColor: viagem.caixa.corCaixa,//troca esse item pela cor da caixa selecionado no cadastro
				spin: false
			});
			
			// configura o marcador com o icone, tooltip e variaveis customizadas:
			var options = {
				icon: _icon,
				viagem: {
					viagemId: viagem.id,
					hospitalPartida: viagem.localPartida.nome,
					hospitalChegada: viagem.localChegada.nome,
					temperaturaAtual: ultimoDetalhe.numTemperaturaDeta,
					temperaturas: viagem.detalhes.map(function (item) {
						return {
							'id': item.id,
							'temperatura': item.numTemperaturaDeta,
							'virou': item.indVirouDeta,
							'tombou': item.indTombouDeta
						};
					})
				}
			};
			
			//######TESTE######
			//Exibir trajeto:
			$.each(viagem.detalhes, function (idx, detalhe) {
				var circle = L.circle([detalhe.numLatitudeDeta, detalhe.numLongitudeDeta], {
				    color: viagem.caixa.corCaixa,
				    fillColor: '#ffffff',
				    fillOpacity: 0.5,
				    radius: 5
				}).addTo(map);
				markers.push(circle);
			});
			//##################
			
			var marker = L.marker([ultimoDetalhe.numLatitudeDeta, ultimoDetalhe.numLongitudeDeta], options).addTo(map)
				.bindTooltip("<b><i class='fa fa-thermometer-empty'></i> Temperatura Atual:</b> " + ultimoDetalhe.numTemperaturaDeta + "ºC.");
			marker.on('click', onMarkerClick); //Adiciona evento que abre o modal.
			markers.push(marker);
		}
	});
}

// Monta um objeto com as coordenadas de acesso do usuário corrente:
function getPositionOptions() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			return { center: [position.coords.latitude, position.coords.longitude], zoom: 12 };
		});
	}
}

// Busca um marcador existente na mapa:
function getMarkerInMap(viagemId) {
	if (markers == null) return null;

	return markers.find(function (item) {
		return item.options.viagemId == viagemId;
	})
}

// Evento chamado ao clicar em algum marcador:
function onMarkerClick(e) {
	// Variáveis:
	var _viagem = e.target.options.viagem;
	
	// Preenche as informações do modal:
	$('#modalLabel').html("<i class='fa fa-plane'></i> Viagem #" + _viagem.viagemId);
	$('#localPartida').val(_viagem.hospitalPartida);
	$('#localChegada').val(_viagem.hospitalChegada);
	
	//Abre modal com gráfico da viagem:
	$('#modalViagem').modal('show');
	
	//Ao fechar, finaliza a coleta de dados do gráfico:
	$("#modalViagem").on("hidden.bs.modal", function () {
		grafico.dispose();
	});
	
	// Inicia a coleta de dados do gráfico de temperatura
	var grafico = new GraficoTemperatura(1, _viagem.viagemId, 'graficoTemperatura');
	grafico.init(_viagem.temperaturas);
}

// Atualizar pesquisa caixa
function atualizarListaCaixas(_caixas){
	
	$('#custom-search-input .list-group').empty();
	
	$('#custom-search-input .list-group').append("<a href='#' class='list-group-item'>Todos</a>");
		
	// Adiciona itens no para seleção:
	$.each(_caixas, function (idx, caixa) {
		$('#custom-search-input .list-group').append("<a href='" + caixa.id 
		+ "' class='list-group-item'><span style='color : " + caixa.corCaixa 
		+ "'><i class='ion-cube'></i></span> " + caixa.idCaixa + "</a>");
	});
	
	buscarItens();
}

function buscarItens(){
    var current_query = $('#search').val().toLowerCase();
	if (current_query !== "") {
		$(".list-group a").hide();
		$(".list-group a").each(function(){
			var current_keyword = $(this).text().toLowerCase();
			if (current_keyword.indexOf(current_query) >=0 || current_keyword == 'todos') {
				$(this).show();    	 	
			};
		});    	
	} else {
		$(".list-group a").show();
	};
}