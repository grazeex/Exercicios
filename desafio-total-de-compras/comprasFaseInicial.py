"""Esse desafio consiste em somar os itens de uma lista de compras.

Fase inicial:
- [x] Crie uma lista com os itens e o valor para uma compra de um supermercado;
- [x] Crie um loop para introduzir os itens na lista;
- [x] Crie um menu com opção de parar ou continuar;
- [x] Mostre a lista e o valor total da compra.

"""

itens = {}
total = 0

while True:
    item = input('Digite o nome do item: ')
    valor = float(input('Digite o valor do item: '))
    itens[item] = valor
    total += valor

    continuar = input('Deseja adicionar outro item? (s/n): ')
    if continuar.lower() != 's':
        break


print('Itens da compra:')
for item, valor in itens.items():
    print(f'{item}: R$ {valor:.2f}')
print(f'Total: R$ {total:.2f}')
