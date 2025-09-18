(function () { // executa assim q for carregado
  const valoresGerados = generatedValues; // atributos gerados
  const formulario = document.getElementById('form-atribuir');
  const seletores = Array.from(document.querySelectorAll('.attr-select'));

  
  function mapearContagem(arr) { // transforma o array em um mapa de contagem
    const mapa = {};
    for (const x of arr) mapa[x] = (mapa[x] || 0) + 1; 
    return mapa;
  }
  const contagensIniciais = mapearContagem(valoresGerados); // guarda qnts valores existem no início

  
  function contagensSelecionadasAtuais() { // lê os selects e  conta qnts vezes o valor foi escolhido (ignora o 'selecione')
    const escolhas = {};
    for (const seletor of seletores) {
      const valor = parseInt(seletor.value, 10);
      if (!isNaN(valor)) escolhas[valor] = (escolhas[valor] || 0) + 1;
    }
    return escolhas;
  }

  function atualizarOpcoes() { // habilita e desabilita opções
    const escolhas = contagensSelecionadasAtuais();
    const restantes = { ...contagensIniciais };

    // tira qnts vezes o valor ja foi escolhido, o 'estoque'
    for (const [valorStr, usado] of Object.entries(escolhas)) {
      const valor = parseInt(valorStr, 10);
      restantes[valor] = (restantes[valor] || 0) - usado;
    }

    // atualiza o select
    for (const seletor of seletores) {
      const atual = seletor.value;
      for (const opcao of seletor.options) {
        if (opcao.value === "" || opcao.value === atual) {
          opcao.disabled = false; 
        } else {
          const valor = parseInt(opcao.value, 10);
          if (isNaN(valor)) continue;
          opcao.disabled = (restantes[valor] || 0) <= 0; // desabilita se n tem mais repetições sobrando
        }
      }
    }
  }

  
  for (const seletor of seletores) { // qnd muda o valor, atualiza para todos os selects
    seletor.addEventListener('change', atualizarOpcoes);
  }

  // exige q use todos os valores para porder dar submit
  formulario.addEventListener('submit', function (e) {
    const escolhas = contagensSelecionadasAtuais();
    const restante = { ...contagensIniciais };
    for (const [valorStr, usado] of Object.entries(escolhas)) {
      const valor = parseInt(valorStr, 10);
      restante[valor] = (restante[valor] || 0) - usado;
    }
    const valido = Object.values(restante).every(c => c === 0);
    if (!valido) {
      e.preventDefault();
      alert('Você precisa usar todos os valores gerados.');
    }
  });

  
  atualizarOpcoes();
})();
