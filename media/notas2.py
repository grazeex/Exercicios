import tkinter as tk


def calcular_media_janela():
    """Calcula a média das notas inseridas na janela."""
    nota1 = float(nota1_spinbox.get())
    nota2 = float(nota2_spinbox.get())
    nota3 = float(nota3_spinbox.get())
    media = (nota1 + nota2 + nota3) / 3
    result_label.config(text=f"A média das notas é: {media:.2f}")

janela = tk.Tk()
janela.title("Cálculo de Média de Notas")

label = tk.Label(janela, text="Entre com as notas:")
label.grid(row=0, column=0, padx=10, pady=10)

nota1_label = tk.Label(janela, text="Nota 1:")
nota1_label.grid(row=1, column=0, padx=10, pady=10)
nota1_spinbox = tk.Spinbox(janela, from_=0, to=10, increment=0.1)
nota1_spinbox.grid(row=1, column=1, padx=10, pady=10)

nota2_label = tk.Label(janela, text="Nota 2:")
nota2_label.grid(row=2, column=0, padx=10, pady=10)
nota2_spinbox = tk.Spinbox(janela, from_=0, to=10, increment=0.1)
nota2_spinbox.grid(row=2, column=1, padx=10, pady=10)

nota3_label = tk.Label(janela, text="Nota 3:")
nota3_label.grid(row=3, column=0, padx=10, pady=10)
nota3_spinbox = tk.Spinbox(janela, from_=0, to=10, increment=0.1)
nota3_spinbox.grid(row=3, column=1, padx=10, pady=10)

button = tk.Button(janela, text="Calcular Média", command=lambda: calcular_media_janela())
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(janela, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()