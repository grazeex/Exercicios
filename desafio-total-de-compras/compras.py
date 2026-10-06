"""Esse desafio consiste em somar os itens de um lista de compras.

Fase estruturada:
- [ ] Organize os código em funções.
- [ ] Crie uma função para salvar a lista e o total em um arquivo txt.
- [ ] Crie uma nova opção no menu para salvar a lista.
"""


def adicionar_item(itens, total):
    item = input('Digite o nome do item: ')
    valor = float(input('Digite o valor do item: '))
    itens.update({item: valor})
    total += valor
    return itens, total


def exibir_itens(itens, total):
    print('Itens da compra:')
    for item, valor in itens.items():
      print(f'{item}: R$ {valor:.2f}')
    print(f'Total: R$ {total:.2f}')



def salvar_lista(itens, total):
    pass


def exibir_menu():
    print('Menu:')
    print('1 - Adicionar item')
    print('2 - Exibir itens e total')
    print('3 - Salvar lista em arquivo')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    return opcao


def main():
    itens = {}
    total = 0.0
    while True:
        opcao =exibir_menu()
        match opcao:
            case '1':
                itens, total = adicionar_item(itens, total)
            case '2':
                exibir_itens(itens, total)
            case '3':
                salvar_lista(itens, total)
            case '4':
                print('Saindo...')
                break
            case _:
                print('Opção inválida!')

if __name__ == '__main__':
    main()