let menuId = $( "#inputCpfId" ).val();

const dados = $.ajax({
    method: "GET",
    url: `https://gateway.gr1d.io/sandbox/dadoscadastrais/v1/consultas/v1/L0011/${menuId}/`,
    accept: "application/json",
    headers: {
        value: '19904100-ab50-4b0b-88aa-e23940426c31',
    },
    dataType: "json"
  });


let botao = $('#botaoEnvida')

let envia = (function dados() {
    event.preventDefault(),
    console.log(botao)
})

   

