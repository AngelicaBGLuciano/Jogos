import tkinter as tk
import random

# Variáveis globais
tentativas = 0
numero_secreto = random.randint(1, 100)

# Função para verificar a adivinhação do jogador
def verificar_adivinhacao():
    global tentativas
    try:
        palpite = int(entry_palpite.get())
        tentativas -= 1  # Decrementa o número de tentativas
        if palpite > 0 and palpite < 101:  # Verifica se está no intervalo válido
            if palpite < numero_secreto:
                label_resultado.config(text=f"Tente um número maior! Tentativas restantes: {tentativas}", fg="blue")
            elif palpite > numero_secreto:
                label_resultado.config(text=f"Tente um número menor! Tentativas restantes: {tentativas}", fg="blue")
            else:
                label_resultado.config(text=f"Parabéns! Você adivinhou o número {numero_secreto}!", fg="green")
                button_verificar.config(state=tk.DISABLED)  # Desabilita o botão após vencer
        else:
            label_resultado.config(text="Número fora do intervalo.", fg="red")

        if tentativas == 0:
            label_resultado.config(text=f"Você perdeu! O número era {numero_secreto}.", fg="red")
            button_verificar.config(state=tk.DISABLED)  # Desabilita o botão após perder
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.", fg="red")


# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)

    label_resultado.config(text="")
    entry_palpite.delete(0, tk.END)
    button_verificar.config(state=tk.NORMAL)  # Habilita o botão de verificar novamente
    
    # Esconde os elementos do jogo
    label_instrucoes.pack_forget()
    entry_palpite.pack_forget()
    button_verificar.pack_forget()
    label_resultado.pack_forget()
    button_reiniciar.pack_forget()

    tela_inicial()
# Função para iniciar o jogo a partir da tela inicial
def iniciar_jogo():
    # Oculta os elementos da tela inicial
    label_inicial.pack_forget()
    easy_button.pack_forget()
    medio_button.pack_forget()
    hard_button.pack_forget()
    

    # Mostra os elementos do jogo
    label_instrucoes.pack()
    entry_palpite.pack(pady=10)
    button_verificar.pack(pady=10)
    label_resultado.pack(pady=10)
    button_reiniciar.pack(pady=10)

# Funções para definir o nível de dificuldade
def nivel_easy():
    global tentativas
    tentativas = 15
    iniciar_jogo()

def nivel_intermediate():
    global tentativas
    tentativas = 10
    iniciar_jogo()

def nivel_hard():
    global tentativas
    tentativas = 5
    iniciar_jogo()

# Função para exibir a tela inicial
def tela_inicial():
    global label_inicial, easy_button, medio_button, hard_button, start_button
    label_inicial = tk.Label(root, text="Bem-vindo ao Jogo de Adivinhação!", font=("courier", 18), bg="#31ffc9")
    label_inicial.pack(pady=20)
    
    # Botões de nível de dificuldade
    easy_button = tk.Button(root, text="Fácil", font=("courier", 14), command=nivel_easy, bg="#6231ff", fg="black")
    easy_button.pack(pady=5)
    
    medio_button = tk.Button(root, text="Médio", font=("courier", 14), command=nivel_intermediate, bg="#ff3168", fg="black")
    medio_button.pack(pady=5)
    
    hard_button = tk.Button(root, text="Difícil", font=("courier", 14), command=nivel_hard, bg="#cfff31", fg="black")
    hard_button.pack(pady=5)

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo de Adivinhação de Números")
root.geometry("600x300")  
root.configure(bg="#31ffc9")  

# Interface gráfica do jogo

# Entrada de número
entry_palpite = tk.Entry(root, font=("courier", 14))

# Labels
label_instrucoes = tk.Label(root, text="Adivinhe um número entre 1 e 100", font=("courier", 14), bg="#31ffc9")
label_resultado = tk.Label(root, text="", font=("courier", 14), bg="#31ffc9")

# Botões
button_verificar = tk.Button(root, text="Verificar", command=verificar_adivinhacao, font=("courier", 12))
button_reiniciar = tk.Button(root, text="Novo Jogo", command=reiniciar_jogo, font=("courier", 12))

# Exibe a tela inicial
tela_inicial()

# Loop principal
root.mainloop()
