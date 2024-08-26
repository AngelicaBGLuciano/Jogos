import tkinter as tk
import random

# Função para verificar a adivinhação do jogador
def verificar_adivinhacao():
    try:
        palpite = int(entry_palpite.get())
        if palpite > 0 and palpite < 101:#intervalo válido
            if palpite < numero_secreto:
                label_resultado.config(text="Tente um número maior!")
            elif palpite > numero_secreto:
                label_resultado.config(text="Tente um número menor!")
            else:
                label_resultado.config(text="Parabéns! Você adivinhou!")
        else:
            label_resultado.config(text="Número fora do intervalo.")
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.")

# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    label_resultado.config(text="")
    entry_palpite.delete(0, tk.END)

# Configuração da janela
root = tk.Tk()
root.title("Jogo de Adivinhação de Números")
root.geometry("400x150")  
root.configure(bg="#31ffc9")  


# Gerar o número secreto
numero_secreto = random.randint(1, 100)


# Interface gráfica

#entrada
entry_palpite = tk.Entry(root)
entry_palpite.place(x=100, y=60)

#labels
label_instrucoes = tk.Label(root, text="Adivinhe um número entre 1 e 100", bg="#31ffc9")
label_instrucoes.place(x=100, y=20)

label_resultado = tk.Label(root, text="", bg="#31ffc9")
label_resultado.place(x=105, y=85)

#botões
button_verificar = tk.Button(root, text="Verificar", command=verificar_adivinhacao)
button_verificar.place(x=250, y=55)

button_reiniciar = tk.Button(root, text="Novo Jogo", command=reiniciar_jogo)
button_reiniciar.place(x=150, y=110)


# Loop
root.mainloop()
