from pathlib import Path

pasta_atual = Path( __file__ ).parent.absolute()

'''
# Abrindo um arquivo para leitura
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    print(lista_de_compras.read())
'''

'''
# Abrindo um arquivo para leitura linha por linha
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    for linha in lista_de_compras: #Usando o for para percorrer cada linha do arquivo
        print(linha.strip())
    linha = lista_de_compras.readline()
    while linha != '': #Enquanto a linha for diferente de vazio mostramos a linha
        print(linha)
        linha = lista_de_compras.readline()
'''
'''
# Abrindo um arquivo para leitura e retornando uma lista com todas as linhas do arquivo
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_compras:
    linhas = lista_compras.readlines()
    print(f'O terceiro item é: {linhas[2]}') #Mostrando a linha 3 do arquivo
    print('Lista:')
    for linha in linhas: #Percorrendo a lista de linhas do arquivo
        print(linha.strip(), end=', ') #Mostrando cada linha da lista sem pular linha
'''

'''
itens_ja_comprados = ['ovos', 'leite']
# Abrindo um arquivo para leitura e escrevendo em outro arquivo apenas os itens que ainda não foram comprados
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_compras:
    itens_lista_compras = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', 'w', encoding='utf-8') as lista_atualizada:
    for item in itens_lista_compras:
        if item.strip() not in itens_ja_comprados:
            lista_atualizada.write(item) # Escrevendo o item no arquivo de lista de compras atualizada
            print(f'Item {item.strip()} adicionado a lista de compras atualizada.')
'''

'''
# Abrindo um arquivo para leitura e escrevendo em outro arquivo apenas os itens que ainda não foram comprados usando list comprehension
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    itens_lista_compras = [item for item in lista_compras.readlines() \
    if not item.replace('\n', '') in itens_ja_comprados]
 
with open(pasta_atual / 'lista_de_compras_atualizada.txt', 'w') as lista_atualizada:
    lista_atualizada.writelines(itens_lista_compras) # Escrevendo todos os itens da lista de compras atualizada no arquivo
'''

# Adicionando itens a lista de compras
itens_a_adicionar = ['farinha', 'fermento']

with open(pasta_atual / 'lista_de_compras.txt', 'a', encoding='utf-8') as lista_compras:
    for item in itens_a_adicionar:
        lista_compras.write(f'\n{item}') # Adicionando o item no arquivo de lista de compras
        print(f'Item {item} adicionado a lista de compras.')
