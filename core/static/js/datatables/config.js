var options = {
  "scrollY": 210, //ativa rolagem vertical - valor define o altura da tabela em px
  "scrollX": true, // ativa barra de rolagem horizontal, quando necessário
  "scrollCollapse": true, // não sei, ainda
  "paging": true, // ativa pagnação da tabela
  "ordering": true,
  "info":     true,

  "aLengthMenu": [[05, 10, 25, 50, 75, 100, -1], [05, 10, 25, 50, 75, 100, "All"]], // opções para quantidade de linhas exibidas
  "iDisplayLength": 10, // padrão para inicio da tabela esta função não funciona com stateSave =true

  stateSave: true, // permite salvar a ultima pesquisa realizada.

  "language": {
    "decimal": ",",
    "thousands": ".",
    "sEmptyTable": "Nenhum registro encontrado",
    "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
    "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
    "sInfoFiltered": "(Filtrados de _MAX_ registros)",
    "sInfoPostFix": "",
    "sInfoThousands": ".",
    "sLengthMenu": "_MENU_ resultados por página",
    "sLoadingRecords": "Carregando...",
    "sProcessing": "Processando...",
    "sZeroRecords": "Nenhum registro encontrado",
    "sSearch": "Pesquisar",
    "oPaginate": {
        "sNext": "Próximo",
        "sPrevious": "Anterior",
        "sFirst": "Primeiro",
        "sLast": "Último"
                  },
    "oAria": {
        "sSortAscending": ": Ordenar colunas de forma ascendente",
        "sSortDescending": ": Ordenar colunas de forma descendente"
              }
            }
 }

$(document).ready(function() { 
  $('#busca').DataTable(options); 
});
