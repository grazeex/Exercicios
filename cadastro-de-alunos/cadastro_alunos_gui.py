import tkinter as tk


def criar_janela():
    janela = tk.Tk()
    janela.geometry("200x250")
    janela.title("Cadastro de Alunos")

    adicionar_widgets(janela)

    janela.mainloop()

def adicionar_widgets(janela):
    global entry_nome, entry_idade, entry_endereco, entry_turma

    tk.Label(janela, text="Cadastro de Alunos").grid(row=0, column=1, pady=10)

    tk.Label(janela, text="Nome").grid(row=1, column=0, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=1, column=1, pady=10)

    tk.Label(janela, text="Idade").grid(row=2, column=0, pady=5)
    entry_idade = tk.Entry(janela)
    entry_idade.grid(row=2, column=1, pady=10)

    tk.Label(janela, text="Endereço").grid(row=3, column=0, pady=5)
    entry_endereco = tk.Entry(janela)
    entry_endereco.grid(row=3, column=1, pady=10)

    tk.Label(janela, text="Turma").grid(row=4, column=0, pady=5)
    entry_turma = tk.Entry(janela)
    entry_turma.grid(row=4, column=1, pady=10)

    tk.Button(janela, text="Cadastrar", command=cadastrar_aluno).grid(row=5, column=0, columnspan=2, pady=10)

    tk.(janela, text="Alunos Cadastrados").grid(row=6, column=1, pady=10)

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()
    turma = entry_turma.get()

    aluno = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "turma": turma
    }

    alunos.append(aluno)
    print("Aluno cadastrado:", aluno)

    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_turma.delete(0, tk.END)

alunos = []

if __name__ == "__main__":
    criar_janela()