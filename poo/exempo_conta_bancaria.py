class Conta:
    """Exemplo de uma classe que representa uma conta bancária."""

    def __init__(self, saldo=0):
        """Inicializa a conta com um saldo inicial."""
        self.__saldo = saldo

    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def obter_saldo(self):
        """Retorna o saldo atual da conta."""
        return self.__saldo


minha_conta = Conta(1000)
minha_conta.depositar(500)
print(f"Saldo atual: R${minha_conta.obter_saldo():.2f}")
