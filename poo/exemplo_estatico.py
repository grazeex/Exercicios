class Matematica:
    @staticmethod
    def adicionar(a, b):
        return a + b

    @classmethod
    def multiplicar(cls, a, b):
        return a * b

print(Matematica.adicionar(2, 3))  # Chamada do método estático
print(Matematica.multiplicar(2, 3))  # Chamada do método de classe
