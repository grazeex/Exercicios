"""Cadastro de alunos
"""

alunos = {}
aluno = {}

def mostrar_menu():
    print("Cadastro de Alunos")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def receber_dados():
    """Recebe os dados do aluno e retorna um dicionário com as informações.

    Returns:
        dict: Dicionário contendo os dados do aluno.
    """
    nome = input("Digite o nome do aluno: ")
    sexo = input("Digite o sexo do aluno (M/F): ")
    endereco = input("Digite o endereço do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno: ")
    rg = input("Digite o RG do aluno: ")

    aluno = {
        "nome": nome,
        "sexo": sexo,
        "endereco": endereco,
        "data_nascimento": data_nascimento,
        "rg": rg
    }
    return aluno, rg

def cadastrado(rg):
    """Verifica se o RG do aluno já está cadastrado.

    Args:
        rg (str): RG do aluno.

    Returns:
        bool: True se o RG já estiver cadastrado, False caso contrário.
    """
    if rg in alunos:
        print("Aluno já cadastrado.")
        return True
    return False

def mostrar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos cadastrados:")
        for rg, aluno in alunos.items():
            print(f"""
            ---------------------------
            Nome: {aluno['nome']}, 
            RG: {rg},
            Sexo: {aluno['sexo']}, 
            Endereço: {aluno['endereco']}, 
            Data de Nascimento: {aluno['data_nascimento']}
            ---------------------------
            """)

while True:
    opcao = mostrar_menu()

    match opcao:
        case "1":   
            aluno, rg = receber_dados()
            if not cadastrado(rg):
                alunos[rg] = aluno
                print("Aluno cadastrado com sucesso!")
            else:
                print("Não foi possível cadastrar o aluno. RG já existente.")

        case "2":
            mostrar_alunos(alunos)
        case "3":
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
