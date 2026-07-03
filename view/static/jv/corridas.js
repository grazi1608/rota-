const API_CORRIDAS = "http://127.0.0.1:5000/corridas";
const API_MOTORISTAS = "http://127.0.0.1:5000/motoristas";

const formCorrida = document.querySelector("#form-corrida");
const campoValor = document.querySelector("#valor");
const campoCusto = document.querySelector("#custo_estimado");
const campoDistancia = document.querySelector("#distancia");
const selectMotorista = document.querySelector("#motorista_id");
const tabelaCorridas = document.querySelector("#tabela-corridas");
const mensagem = document.querySelector("#mensagem");
const botaoRecarregar = document.querySelector("#botao-recarregar");

function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = `mensagem ${tipo}`;
}

function limparFormulario() {
    campoValor.value = "";
    campoCusto.value = "";
    campoDistancia.value = "";
    selectMotorista.value = "";
}

async function carregarMotoristas() {
    try {
        const resposta = await fetch(API_MOTORISTAS);
        const motoristas = await resposta.json();
        selectMotorista.innerHTML = '<option value="">Selecione um motorista...</option>';
        motoristas.forEach(m => {
            const opt = document.createElement("option");
            opt.value = m.id;
            opt.textContent = m.nome;
            selectMotorista.appendChild(opt);
        });
    } catch (err) {
        mostrarMensagem("Erro ao carregar motoristas.", "erro");
    }
}

async function listarCorridas() {
    try {
        const resposta = await fetch(API_CORRIDAS);
        const corridas = await resposta.json();
        tabelaCorridas.innerHTML = "";

        if (corridas.length === 0) {
            tabelaCorridas.innerHTML = `<tr><td colspan="7">Nenhuma corrida registrada.</td></tr>`;
            return;
        }

        corridas.forEach(c => {
            const dataFormatada = c.data_hora;
            const linha = document.createElement("tr");
            linha.innerHTML = `
                <td data-label="ID">${c.id}</td>
                <td data-label="Data/Hora">${dataFormatada}</td>
                <td data-label="Valor">R$ ${parseFloat(c.valor).toFixed(2)}</td>
                <td data-label="Custo">R$ ${parseFloat(c.custo_estimado).toFixed(2)}</td>
                <td data-label="Lucro" style="color: green; font-weight: bold;">R$ ${parseFloat(c.lucro).toFixed(2)}</td>
                <td data-label="Distância">${c.distancia} km</td>
                <td data-label="Ações">
                    <button class="perigo" onclick="deletarCorrida(${c.id})">Excluir</button>
                </td>
            `;
            tabelaCorridas.appendChild(linha);
        });
    } catch (err) {
        mostrarMensagem("Erro ao carregar o histórico de corridas.", "erro");
    }
}

async function salvarCorrida(e) {
    e.preventDefault();
    const dados = {
        valor: parseFloat(campoValor.value),
        custo_estimado: parseFloat(campoCusto.value),
        distancia: parseFloat(campoDistancia.value),
        motorista_id: parseInt(selectMotorista.value)
    };

    try {
        const resposta = await fetch(API_CORRIDAS, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        if (!resposta.ok) {
            mostrarMensagem("Erro ao salvar corrida.", "erro");
            return;
        }

        mostrarMensagem("Corrida registrada com sucesso!", "sucesso");
        limparFormulario();
        listarCorridas();
    } catch (err) {
        mostrarMensagem("Erro de conexão com o servidor.", "erro");
    }
}

async function deletarCorrida(id) {
    if (!confirm("Remover esta corrida do histórico?")) return;
    try {
        const resposta = await fetch(`${API_CORRIDAS}/${id}`, { method: "DELETE" });
        if (resposta.ok) {
            mostrarMensagem("Corrida excluída com sucesso.", "sucesso");
            listarCorridas();
        }
    } catch (err) {
        mostrarMensagem("Erro ao excluir a corrida.", "erro");
    }
}

formCorrida.addEventListener("submit", salvarCorrida);
botaoRecarregar.addEventListener("click", () => { carregarMotoristas(); listarCorridas(); });

// Inicializar dados na página
carregarMotoristas();
listarCorridas();