import random
import tkinter as tk


## Faz a jenela aparecer no centro da tela
# Obtém as dimensões da tela do usuário
largura = 500
altura = 400

janela = tk.Tk()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula a posição X e Y para o centro
pos_x = int((largura_tela / 2) - (largura / 2))
pos_y = int((altura_tela / 2) - (altura / 2))

# Aplica a geometria final
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


def gerar_palpite():
    numero = random.sample(range(1, 61), 6)
    resultado_label.config(text=f"Palpite da Mega-Sena: {sorted(numero)}")
janela.title("Palpite da Mega-Sena")

label = tk.Label(janela, text="Clique no botão para gerar um palpite da Mega-Sena")
label.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

botao = tk.Button(janela, text="Gerar Palpite", command=lambda: gerar_palpite())
botao.pack(pady=10)

janela.mainloop()