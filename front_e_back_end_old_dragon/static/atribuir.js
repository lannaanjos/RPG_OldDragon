(function () {
  const generated = generatedValues; // ex.: [13,13,14,9,10,9]
  const form = document.getElementById('form-atribuir');
  const selects = Array.from(document.querySelectorAll('.attr-select'));

  // Mapeia quantas vezes cada valor aparece originalmente
  function countMap(arr) {
    const m = {};
    for (const x of arr) m[x] = (m[x] || 0) + 1;
    return m;
  }
  const baseCounts = countMap(generated);

  // Conta quantas vezes já foram usados nas seleções atuais
  function currentSelectionCounts() {
    const picks = {};
    for (const sel of selects) {
      const v = parseInt(sel.value, 10);
      if (!isNaN(v)) picks[v] = (picks[v] || 0) + 1;
    }
    return picks;
  }

  function refreshOptions() {
    const picks = currentSelectionCounts();
    const remaining = { ...baseCounts };

    // Remove usos atuais do total restante
    for (const [valStr, used] of Object.entries(picks)) {
      const val = parseInt(valStr, 10);
      remaining[val] = (remaining[val] || 0) - used;
    }

    // Atualiza cada select
    for (const sel of selects) {
      const current = sel.value;
      for (const opt of sel.options) {
        if (opt.value === "" || opt.value === current) {
          opt.disabled = false; // vazio sempre permitido, atual sempre permitido
        } else {
          const v = parseInt(opt.value, 10);
          if (isNaN(v)) continue;
          opt.disabled = (remaining[v] || 0) <= 0;
        }
      }
    }
  }

  // Listener para cada select
  for (const sel of selects) {
    sel.addEventListener('change', refreshOptions);
  }

  // Validação final: precisa usar exatamente todos os valores
  form.addEventListener('submit', function (e) {
    const picks = currentSelectionCounts();
    const rem = { ...baseCounts };
    for (const [valStr, used] of Object.entries(picks)) {
      const val = parseInt(valStr, 10);
      rem[val] = (rem[val] || 0) - used;
    }
    const ok = Object.values(rem).every(c => c === 0);
    if (!ok) {
      e.preventDefault();
      alert('Você precisa usar exatamente todos os valores gerados, sem repetir além do permitido.');
    }
  });

  // Inicializa estado
  refreshOptions();
})();
