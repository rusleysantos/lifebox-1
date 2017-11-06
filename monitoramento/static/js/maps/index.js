// Variaveis globais:
var map;
var refreshTime = (1 * 1000);
var markers = [];
var idViagemAtual;

// Inicializando o mapa do OpenStreetMap:
function initmap() {
    map = new L.Map('map', getPositionOptions());

    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osm = new L.TileLayer(osmUrl);
    map.setView(new L.LatLng(-20.297618, -40.295777), 10);
    map.addLayer(osm);

    //Atualiza os marcadores a cada x milisegundos:
    setInterval(function () {
        $.when(getData()).done(function (viagens) {
            createUpdateMarkers(viagens);
        });
    }, refreshTime);
}


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
            console.log("Não foi possivel coletar as viagens ativas no sistema. Entre em contato com o administrador do Sistema.")
        }
    });
}

function createUpdateMarkers(viagens) {
    //Verifica se existem viagens:
    if (viagens == null || viagens.length == 0) return;

    $.each(viagens, function (idx, viagem) {
        if (viagem.detalhes != null) {
            // Pega o ultimo detalhe (ultima localização):
            var ultimoDetalhe = viagem.detalhes[viagem.detalhes.length - 1];

            //Cria o icone do marcador com a cor informada no cadastro:
            var options = {
                icon: L.AwesomeMarkers.icon(
                    {
                        icon: 'cube',
                        prefix: 'ion',
                        markerColor: 'white',//valores possiveis: 'red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'
                        iconColor: '#165b97',//troca esse item pela cor da caixa selecionado no cadastro
                        spin: false
                    }
                ),
                tooltip: {
                    html: "my tooltip text"
                },
                //minhas variaveis de controle:
                viagemId: viagem.id,
                hospitalPartida: viagem.localPartida.nome,
                hospitalChegada: viagem.localChegada.nome,
                temperaturaAtual: ultimoDetalhe.numTemperaturaDeta,
                temperaturas: viagem.detalhes.map(function (item) {
                    return item.numTemperaturaDeta
                })
            };

            // Caso a viagem já exista no mapa, seus dados são atualizados:
            var marker = getMarkerInMap(viagem.id);
            if (markers != null && marker != null) {
                marker.setLatLng(new L.LatLng(ultimoDetalhe.numLatitudeDeta, ultimoDetalhe.numLongitudeDeta));
                    // .bindPopup("<b><i class='fa fa-thermometer-empty'></i> Temperatura Atual:</b> " + ultimoDetalhe.numTemperaturaDeta + "ºC.");
            }
            // Caso contrário, adiciona o novo marcador:
            else {
                marker = L.marker([ultimoDetalhe.numLatitudeDeta, ultimoDetalhe.numLongitudeDeta], options)
                    .addTo(map);
                    // .bindPopup("<b><i class='fa fa-thermometer-empty'></i> Temperatura:</b> " + ultimoDetalhe.numTemperaturaDeta + "ºC.");

                // Armazena os marcadores cadastrados:
                markers.push(marker);
            }

            // Adiciona ação ao clicar sobre o marcador:
            marker.on('click', onMarkerClick);
        }
    });
}

function getPositionOptions() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            return { center: [position.coords.latitude, position.coords.longitude], zoom: 12 };
        });
    }
}

function getMarkerInMap(viagemId) {
    if (markers == null) return null;

    return markers.find(function (item) {
        return item.options.viagemId == viagemId;
    })
}

function onMarkerClick(e) {
    idViagemAtual = e.target.options.viagemId;

    var grafico = new GraficoTemperatura(1, idViagemAtual, 'graficoTemperatura');
    grafico.init();

    //preenche dados do modal:
    $('#modalLabel').html(
        "<i class='fa fa-plane'></i> Viagem #" + idViagemAtual
    );
    $('#trajeto').html(
        "<i class='fa fa-hospital-o'></i>" + e.target.options.hospitalPartida
        + "  <i class='fa fa-angle-double-right'></i>  "
        + " <i class='fa fa-hospital-o'></i>" + e.target.options.hospitalChegada
    );
    //abre modal com gráficos da viagem:
    $('#modalViagem').modal('show');
    $("#modalViagem").on("hidden.bs.modal", function () {
        grafico.dispose();
    });
    // $('#modalViagem').modal('dismiss', function(){
    //     grafico.dispose();
    // })
}

// function carregarDadosGraficoTemperatura(viagemId) {
//     var marker = getMarkerInMap(viagemId);
//     $("#grafico")
//         .sparkline(marker.options.temperaturas, {
//             type: 'line',
//             width: '100%',
//             height: '100%',
//             lineColor: '#4ba5a5',
//             fillColor: '#ffffff',
//             spotColor: undefined,
//             minSpotColor: '#3f007f',
//             maxSpotColor: '#bf0000',
//             highlightSpotColor: '#4ba5a5',
//             highlightLineColor: '#4ba5a5',
//             spotRadius: 5
//         });

// }
