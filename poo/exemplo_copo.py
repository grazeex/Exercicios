class Copo:
    """Representa um copo com capacidade de encher e beber água.
    """
    def __init__(self, volume):
        self.volume = volume
        print("Copo criado com volume:", volume)

    def encher(self):
        print("O copo está cheio.")

    def beber(self):
        print("Você bebeu a água")

    def __del__(self):
        print("Copo destruído.")

meu_copo = Copo(500)
meu_copo.encher()
meu_copo.beber()
quantidade = meu_copo.volume
print(f"O copo tem capacidade de {quantidade} ml.")
del meu_copo
outro_copo = Copo(300)
outro_copo.encher()
outro_copo.beber()