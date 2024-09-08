const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const wordDiv = document.getElementById('word');
const lettersDiv = document.getElementById('letters');

let palavras = []; // Este array será preenchido com palavras do arquivo

// Função para carregar palavras do arquivo
async function carregarPalavras() {
    const response = await fetch('palavras.txt');
    const text = await response.text();
    palavras = text.split('\n').map(p => p.trim().toUpperCase());
}


const letrasCorretas = [];
const letrasErradas = [];
const maxErros = 7;
let palavra = '';

function desenhaForca() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 2;

    // Desenha a base da forca
    ctx.beginPath();
    ctx.moveTo(50, 350);
    ctx.lineTo(150, 350);
    ctx.moveTo(100, 350);
    ctx.lineTo(100, 50);
    ctx.lineTo(250, 50);
    ctx.lineTo(250, 100);
    ctx.stroke();
}

function desenhaBoneco(erros) {
    ctx.lineWidth = 2;

    switch (erros) {
        case 1: // Cabeça
            ctx.beginPath();
            ctx.arc(250, 130, 30, 0, Math.PI * 2);
            ctx.stroke();
            break;
        case 2: // Corpo
            ctx.beginPath();
            ctx.moveTo(250, 160);
            ctx.lineTo(250, 250);
            ctx.stroke();
            break;
        case 3: // Braço esquerdo
            ctx.beginPath();
            ctx.moveTo(250, 180);
            ctx.lineTo(200, 220);
            ctx.stroke();
            break;
        case 4: // Braço direito
            ctx.beginPath();
            ctx.moveTo(250, 180);
            ctx.lineTo(300, 220);
            ctx.stroke();
            break;
        case 5: // Perna esquerda
            ctx.beginPath();
            ctx.moveTo(250, 250);
            ctx.lineTo(200, 300);
            ctx.stroke();
            break;
        case 6: // Perna direita
            ctx.beginPath();
            ctx.moveTo(250, 250);
            ctx.lineTo(300, 300);
            ctx.stroke();
            break;
    }
}

function atualizaPalavra() {
    const displayPalavra = palavra.split('').map(letra => (letrasCorretas.includes(letra) ? letra : '_')).join(' ');
    wordDiv.textContent = displayPalavra;
}

function verificaVitoria() {
    if (palavra.split('').every(letra => letrasCorretas.includes(letra))) {
        alert('Você ganhou!');
        location.reload();
    }
}

function verificaDerrota() {
    if (letrasErradas.length >= maxErros) {
        alert('Você perdeu! A palavra era ' + palavra);
        location.reload();
    }
}

function inicializaLetras() {
    const alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    alfabeto.split('').forEach(letra => {
        const letraButton = document.createElement('button');
        letraButton.textContent = letra;
        letraButton.addEventListener('click', () => {
            letraButton.disabled = true;
            if (palavra.includes(letra)) {
                letrasCorretas.push(letra);
                atualizaPalavra();
                verificaVitoria();
            } else {
                letrasErradas.push(letra);
                desenhaBoneco(letrasErradas.length);
                verificaDerrota();
            }
        });
        lettersDiv.appendChild(letraButton);
    });
}

function inicializaJogo() {
    desenhaForca();
    atualizaPalavra();
    inicializaLetras();
}

// Função principal que inicia o jogo após carregar as palavras
async function start() {
    await carregarPalavras();  // Aguarda o carregamento do arquivo .txt
    palavra = palavras[Math.floor(Math.random() * palavras.length)]; // Seleciona uma palavra aleatória
    inicializaJogo();
}

start(); // Inicia o jogo
