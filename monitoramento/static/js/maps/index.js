var map;
var osm;
var markers = [];

// Inicializando o mapa do openstreetmap no index
function initmap() {


    map = new L.Map('map', getPositionOptions());

    // create the tile layer with correct attribution
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    osm = new L.TileLayer(osmUrl);
    map.setView(new L.LatLng(-20.297618, -40.295777), 10);
    map.addLayer(osm);
    getData();

    //teste para verificar alteração de coordenadas:
    setTimeout(function () {
        var marker = markers[0];
        marker.setLatLng(new L.LatLng(-20.3116012, -40.3098049));
    }, 5000);
}

function getData() {
    var latitude;
    var longitude;
    var temperatura;
    var color;

    $.ajax({
        type: "get",
        url: "/api/detalhe/",
        cache: false,
        Accept: "application/json",
        contentType: "application/json",
        success: function (response) {
            $.each(response, function (idx, obj) {
                $.each(obj, function (key, value) {
                    if (key == "numLatitudeDeta") {
                        latitude = value
                    }
                    if (key == "numLongitudeDeta") {
                        longitude = value;
                    }
                    if (key == "numTemperaturaDeta") {
                        temperatura = value;
                    }
                    color = 'red';
                    if (latitude != null && longitude != null && temperatura != null && color != null) {
                        //Seleciona a cor da caixa:
                        var icon = {
                            icon: L.AwesomeMarkers.icon(
                                {
                                    icon: 'cube',
                                    prefix: 'ion',
                                    markerColor: 'white',//values: 'red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'
                                    iconColor: '#165b97',//troca esse item pela cor da caixa selecionado no cadastro
                                    spin: false
                                }
                            )
                        };

                        var marker = L.marker([latitude, longitude], icon).addTo(map).bindPopup("<b>Temperatura: </b>" + temperatura + "ºC. ");
                        markers.push(marker);
                        latitude = longitude = temperatura = null;
                    }
                });
            });

        },
        error: function (response, status, error) {
            alert("Que coisa feia ... deu erro");
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
