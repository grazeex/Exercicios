class Veiculo:
    quantidade_de_veiculos = 0
    def __init__(self, marca, modelo, ano, cor="preto"):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        Veiculo.quantidade_de_veiculos += 1

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}"

    def mover(self):
        pass

class Carro(Veiculo):    
    def exibir_informacoes(self):
        return f"Carro - Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}"

    def mover(self):
        return "Estou dirigindo o carro."
    
class Moto(Veiculo):    
    def exibir_informacoes(self):
        return f"Moto - Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}"

    def mover(self):
        return "A moto está se movendo."

class Bicicleta(Veiculo):
    
    def exibir_informacoes(self):
        return f"Bicicleta - Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}"

    def mover(self):
        return "Estou pedalando na bicicleta."

# Exemplo de função polimorifica
def mover_veiculo(veiculo):
   return veiculo.mover()

meu_carro = Carro("Toyota", "Corolla", 2020)
outro_carro = Carro("Honda", "Civic", 2021)
mais_um_carro = Carro("Ford", "Mustang", 2022)
minha_moto = Moto("Honda", "CBR300", 2020)
minha_bicicleta = Bicicleta("Trek", "Marlin", 2020, "Azul")
print(meu_carro.exibir_informacoes())
print(outro_carro.exibir_informacoes())
print(mais_um_carro.exibir_informacoes())
print(minha_moto.exibir_informacoes())
print(minha_bicicleta.exibir_informacoes())
print(mover_veiculo(meu_carro))
print(mover_veiculo(minha_moto))
print(mover_veiculo(minha_bicicleta))
print(f"Quantidade de veículos: {Veiculo.quantidade_de_veiculos}")
