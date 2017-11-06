var GraficoTemperatura = function (_secondsUpdate, _idViagem, _element) {
    this.tempuraturas = [];
    this.morrisElement;

    this.refresh = _secondsUpdate * 1000;
    this.id = _idViagem;
    this.element = _element;
    this.execution;
};

GraficoTemperatura.prototype.init = function () {
    var _this = this;
    
    //Atualiza os marcadores a cada x milisegundos:
    _this.execution = setInterval(function () {
        $.when(_this.getDataGraficoTemperaturas()).done(function (viagem) {
            $('#' + _this.element).empty();

            _this.morrisElement = new Morris.Line({
                element: _this.element,
                data: viagem.detalhes.map(function (item) {
                    return {
                        'id': item.id,
                        'temperatura': item.numTemperaturaDeta,
                        'virou': item.indVirouDeta,
                        'tombou': item.indTombouDeta
                    };
                }),
                xkey: 'id',
                ykeys: ['temperatura'],
                labels: ['Temperatura'],
                resize: true,
                hoverCallback: function (index, options, content, row) {
                    return "<b>Temperatura</b>: " + row.temperatura + "ºC"
                        + "</br><b>Virou</b>: " + (row.virou ? 'Sim' : 'Não')
                        + "</br><b>Tombou</b>: " + (row.tombou ? 'Sim' : 'Não');
                }
            });
        });
    }, _this.refresh);
};

GraficoTemperatura.prototype.getDataGraficoTemperaturas = function () {
    var _this = this;

    return $.ajax({
        type: "get",
        url: "/api/viagem/" + _this.id,
        cache: false,
        Accept: "application/json",
        contentType: "application/json",
        success: function (response) {
            return response;
        },
        error: function (response, status, error) {
            console.log("Não foi possivel coletar as temperaturas da viagem " + _this.id + ". Entre em contato com o administrador do Sistema.");
        }
    });
};

GraficoTemperatura.prototype.dispose = function () {
    clearInterval(this.execution);
}

