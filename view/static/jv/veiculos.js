const API_VEICULOS = "http://127.0.0.1:5000/veiculos";
const API_MOTORISTAS = "http://127.0.0.1:5000/motoristas";

const formVeiculo = document.querySelector("#form-veiculo");
const veiculoId = document.querySelector("#veiculo-id");
const campoMarca = document.querySelector("#marca");
const campoModelo = document.querySelector("#modelo");
const campoPlaca = document.querySelector("#placa");
const campoAno = document.querySelector("#ano");
const selectMotorista = document.querySelector("#motorista_id");
const tabelaVeiculos = document.querySelector("#tabela-veiculos");
const mensagem = document.querySelector("#mensagem");
const tituloFormulario = document.querySelector("#titulo-formulario");
const botaoSalvar = document.querySelector("#botao-salvar");
const botaoCancelar = document.querySelector("#botao-cancelar");
const botaoRecarregar = document.querySelector("#botao-recarregar");

function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = `mensagem ${tipo}`;
}

function limparFormulario() {
    veiculoId.value = "";
    campoMarca.value = "";
    campoModelo.value = "";
    campoPlaca.value = "";
    campoAno.value = "";
    selectMotorista.value = "";
    tituloFormulario.textContent = "Cadastrar veículo";
    botaoSalvar.textContent = "Salvar";
}

async function carregarMotoristas() {
    try {
        const resposta = await fetch(API_MOTORISTAS);
        const motoristas = await resposta.json();
        
        selectMotorista.innerHTML = '<option value="">Selecione um motorista...</option>';
        
        motoristas.forEach(motorista => {
            const opcao = document.createElement("option");
            opcao.value = motorista.id;
            opcao.textContent = `${motorista.nome} (ID: ${motorista.id})`;
            selectMotorista.appendChild(opcao);
        });
    } catch (erro) {
        mostrarMensagem("Erro ao carregar a lista de motoristas.", "erro");
    }
}

async function listarVeiculos() {
    try {
        const resposta = await fetch(API_VEICULOS);
        const veiculos = await resposta.json();

        tabelaVeiculos.innerHTML = "";

        if (veiculos.length === 0) {
            tabelaVeiculos.innerHTML = `
                <tr>
                    <td colspan="5">Nenhum veículo cadastrado.</td>
                </tr>
            `;
            return;
        }

        veiculos.forEach((veiculo) => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td data-label="ID">${veiculo.id}</td>
                <td data-label="Modelo">${veiculo.modelo}</td>
                <td data-label="Placa">${veiculo.placa}</td>
                <td data-label="Ano">${veiculo.ano}</td>
                <td data-label="Ações">
                    <div class="acoes-tabela">
                        <button onclick='prepararEdicao(${JSON.stringify(veiculo)})'>Editar</button>
                        <button class="perigo" onclick="deletarVeiculo(${veiculo.id})">Excluir</button>
                    </div>
                </td>
            `;

            tabelaVeiculos.appendChild(linha);
        });
    } catch (erro) {
        mostrarMensagem("Não foi possível carregar os veículos. Verifique se a API está ativa.", "erro");
    }
}

function prepararEdicao(veiculo) {
    veiculoId.value = veiculo.id;
    campoMarca.value = veiculo.marca;
    campoModelo.value = veiculo.modelo;
    campoPlaca.value = veiculo.placa;
    campoAno.value = veiculo.ano;
    selectMotorista.value = veiculo.motorista_id || "";
    tituloFormulario.textContent = "Editar veículo";
    botaoSalvar.textContent = "Atualizar";
    mostrarMensagem("Editando veículo selecionado.", "sucesso");
}

async function salvarVeiculo(evento) {
    evento.preventDefault();

    const dados = {
        marca: campoMarca.value,
        modelo: campoModelo.value,
        placa: campoPlaca.value,
        ano: parseInt(campoAno.value),
        motorista_id: parseInt(selectMotorista.value)
    };

    const id = veiculoId.value;
    const metodo = id ? "PUT" : "POST";
    const url = id ? `${API_VEICULOS}/${id}` : API_VEICULOS;

    try {
        const resposta = await fetch(url, {
            method: metodo,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dados),
        });

        if (!resposta.ok) {
            const erro = await resposta.json();
            mostrarMensagem(erro.error || "Erro ao salvar veículo.", "erro");
            return;
        }

        mostrarMensagem(id ? "Veículo atualizado com sucesso." : "Veículo cadastrado com sucesso.", "sucesso");
        limparFormulario();
        listarVeiculos();
    } catch (erro) {
        mostrarMensagem("Erro de conexão com a API.", "erro");
    }
}

async function deletarVeiculo(id) {
    const confirmar = confirm("Deseja realmente excluir este veículo?");

    if (!confirmar) {
        return;
    }

    try {
        const resposta = await fetch(`${API_VEICULOS}/${id}`, {
            method: "DELETE",
        });

        if (!resposta.ok) {
            const erro = await resposta.json();
            mostrarMensagem(erro.error || "Erro ao excluir veículo.", "erro");
            return;
        }

        mostrarMensagem("Veículo excluído com sucesso.", "sucesso");
        listarVeiculos();
    } catch (erro) {
        mostrarMensagem("Erro de conexão com a API.", "erro");
    }
}

formVeiculo.addEventListener("submit", salvarVeiculo);
botaoCancelar.addEventListener("click", limparFormulario);
botaoRecarregar.addEventListener("click", () => {
    carregarMotoristas();
    listarVeiculos();
});

// Inicialização da página
carregarMotoristas();
listarVeiculos();