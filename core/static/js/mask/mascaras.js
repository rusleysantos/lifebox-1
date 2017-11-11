
$(function () {
    $(document).ready(function() {
        //Mascara para datas
        $(".date").mask("99/99/9999",{placeholder:"dd/mm/yyyy"});

        //Mascara para Equipamentos
        $(".eq_mask")
        .mask("aa-999",{placeholder:"EQ-___"})
        .focusout(function (event) {
            var target, eq_mask, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            eq_mask = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            lement.mask("aa-999");
        });

        //Mascara para Caixas
        $(".cx_mask")
        .mask("aa-999",{placeholder:"CX-___"})
        .focusout(function (event) {
            var target, cx_mask, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            cx_mask = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            lement.mask("aa-999");
        });

        //Mascara para Imei Sim Card
        $(".imeiSimCard")
        .mask("99999.99999.99999.99999-99")
        .focusout(function (event) {
            var target, imeicard, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            imeicard = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            element.mask("99999.99999.99999.99999-99");
        });

        //Mascara para Imei Rastreadores, celular, arduino;
        $(".imeiTracker")
        .mask("99999.99999.99999")
        .focusout(function (event) {
            var target, imeicel, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            imeicel = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            element.mask("99999.99999.99999");
        });

        //Mascara para CEPs
        $(".cep")
        .mask("99.999-999")
        .focusout(function (event) {
            var target, cep, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            cep = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            element.mask("99.999-999");
        });

        //Mascara para telefones Fixo ou Celular;
        $(".phone")
            .mask("(99) 99999-999?9")
            .focusout(function (event) {
                var target, phone, element;
                target = (event.currentTarget) ? event.currentTarget : event.srcElement;
                phone = target.value.replace(/\D/g, '');
                element = $(target);
                element.unmask();
                if(phone.length > 10) {
                    element.mask("(99) 99999-9999");
                } else {
                    element.mask("(99) 9999-9999?");
                }
            });

            //Mascara para limpar campos relativos a CEPs
        function limpa_formulário_cep() {
            // Limpa valores do formulário de cep.
            $("#id_logradouro").val("");
            $("#id_bairro").val("");
            $("#id_cidade").val("");
            $("#id_uf").val("");
        }

        //Quando o campo cep perde o foco.
        $("#id_cep").blur(function() {

            //Nova variável "cep" somente com dígitos.
            var cep = $(this).val().replace(/\D/g, '');

            //Verifica se campo cep possui valor informado.
            if (cep != "") {

                //Expressão regular para validar o CEP.
                var validacep = /^[0-9]{8}$/;

                //Valida o formato do CEP.
                if(validacep.test(cep)) {

                    //Preenche os campos com "..." enquanto consulta webservice.
                    $("#id_logradouro").val("...");
                    $("#id_bairro").val("...");
                    $("#id_cidade").val("...");
                    $("#id_uf").val("...");

                    //Consulta o webservice viacep.com.br/
                    $.getJSON("//viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                        if (!("erro" in dados)) {
                            //Atualiza os campos com os valores da consulta.
                            $("#id_logradouro").val(dados.logradouro);
                            $("#id_bairro").val(dados.bairro);
                            $("#id_cidade").val(dados.localidade);
                            $("#id_uf").val(dados.uf);
                        } //end if.
                        else {
                            //CEP pesquisado não foi encontrado.
                            limpa_formulário_cep();
                            alert("CEP não encontrado.");
                        }
                    });
                } //end if.
                else {
                    //cep é inválido.
                    limpa_formulário_cep();
                    alert("Formato de CEP inválido.");
                }
            } //end if.
            else {
                //cep sem valor, limpa formulário.
                limpa_formulário_cep();
            }
        });
    });
});
