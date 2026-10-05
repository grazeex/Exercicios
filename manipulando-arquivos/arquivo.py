"""https://jocile.com/notas/python/manipulando-arquivos/caminhos-com-pathlib"""
import os
from pathlib import Path

'''
# Conhecendo o Path
print(Path('primeira_pasta/segunda_pasta'))
print(type(Path('primeira_pasta/segunda_pasta')))
'''

'''
# Fazendo um loop para acessar os arquivos
for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    print(Path('primeira_pasta/segunda_pasta') / nome)
'''

'''
# Verificar o diretório home do usuário
print(Path.home())
'''
'''
# Verificar o diretório atual
print(Path.cwd())
'''

'''
# Mudar diretório de trabalho
os.chdir(Path.home())
print(Path.cwd())
'''

'''
# Verificar se é absoluto
print(Path.cwd().is_absolute()) # True
print(Path('primeira_pasta').is_absolute()) # False
 
# Transformar relativo em absoluto
print(Path.cwd() / Path('primeira_pasta'))
'''

'''
# Caminho da pasta onde o script está localizado
print(Path(__file__).parent.absolute())
'''

'''
# Acessar partes do caminho
p = Path('C:/Users/Aluno/spam.txt')
print(f'Drive: {p.anchor}')  # 'C:\'
print(f'Pasta raiz do usuário no Windows: {p.parent}')  # WindowsPath('C:/Users/Al')
print(f'Nome do arquivo: {p.name}')    # 'spam.txt'
print(f'Nome do arquivo sem extensão: {p.stem}')    # 'spam'
print(f'Extensão do arquivo: {p.suffix}')  # '.txt'
print(f'Drive: {p.drive}')   # 'C:'

# Acessar hierarquia superior
print(f'Pasta superior: {p.parents[0]}') # C:/Users/Aluno
print(f'Pasta acima da superior: {p.parents[1]}') # C:/Users
print(f'Pasta superior do diretório atual: {Path.cwd().parents[0]}')
'''

# Listando arquivos e pastas
# print(list(Path.home().glob('*'))) # Lista tudo
# print(list(Path.home().glob('*.txt'))) # Lista apenas arquivos .txt

# print(list(Path.cwd().glob('*'))) # Lista tudo do diretório do repositório atual

print(list(Path(__file__).parent.absolute().glob('*'))) # Listando arquivos e pastas do diretório onde o script está localizado
