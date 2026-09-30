"""Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de listar de notas crie uma app com janelas em Python para receber 3 notas e mostrar a média

Algoritmo:
1. [x] Receber 3 notas do usuário
2. [x] Calcular a média das notas
3. [x] Mostrar a média no console
4. [x] Organizar o código em funções
5. [x] Mostrar a média usando janelas

"""


def receber_nota_console():
    nota = float(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        return receber_nota_console()
    return nota


def calcular_media(nota1, nota2, nota3):
    """Calcula a média de 3 notas.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.
        nota3 (float): A terceira nota.

    Returns:
        float: A média das três notas.
    """
    media = (nota1 + nota2 + nota3) / 3
    return media

def mostrar_media_console(media):
    """Mostra a média no console.

    Args:
        media (float): A média das notas.
    """
    nota1 = receber_nota_console()
    nota2 = receber_nota_console()
    nota3 = receber_nota_console()
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das notas é: {media:.2f}")

import tkinter as tk

janela = tk.Tk()


def mostrar_janela():
    """Mostra a média em uma janela usando Tkinter."""
    janela.configure(bg="lightblue")
    janela.title("Cálculo de Média de Notas")
    #janela.geometry("400x300")

    label = tk.Label(janela, text="Entre com as notas:", bg="lightblue", font=("Arial", 14))
    label.grid(row=0, column=0, padx=50, pady=30)

    input_nota1 = tk.Entry(janela, font=("Arial", 12))
    input_nota1.grid(row=1, column=0, padx=50, pady=10)
    input_nota2 = tk.Entry(janela, font=("Arial", 12))
    input_nota2.grid(row=2, column=0, padx=50, pady=10)
    input_nota3 = tk.Entry(janela, font=("Arial", 12))
    input_nota3.grid(row=3, column=0, padx=50, pady=10)

    label2 = tk.Label(janela, text="", bg="lightblue", font=("Arial", 12))
    label2.grid(row=4, column=0, padx=50, pady=10)
    button = tk.Button(
        janela,
        text="Calcular Média",
        command=lambda: exibe_media_janela(
            label2,
            float(input_nota1.get()),
            float(input_nota2.get()),
            float(input_nota3.get()),
        ),
        bg="lightblue",
        font=("Arial", 12),
    )
    button.grid(row=5, column=0, padx=50, pady=50)

    return label2, input_nota1, input_nota2, input_nota3


def exibe_media_janela(label2, nota1, nota2, nota3):
    """Mostra a média em uma janela usando Tkinter."""
    media = calcular_media(nota1, nota2, nota3)

    label2.config(text=f"A média das notas é: {media:.2f}")

def main():
    # mostrar_media_console(calcular_media)
    mostrar_janela()


main()
janela.mainloop()
