"""Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de listar de notas crie uma app com janelas em Python para receber 3 notas e mostrar a média

Algoritmo:
1. [x] Receber 3 notas do usuário
2. [x] Calcular a média das notas
3. [x] Mostrar a média no console
4. [x] Criar funções
5. [ ] Criar janelas

"""


def receber_nota():
    nota = float(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        return receber_nota()
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


nota1 = receber_nota()
nota2 = receber_nota()
nota3 = receber_nota()
media = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {media}")
