class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return "[Código {} - Saldo {}]".format(self.codigo, self.saldo)

    def deposita(self, valor):
        self.saldo += valor



def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(100)

print(conta_do_gui)
print(conta_da_dani)

conta_da_dani.deposita(300)

print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
print(contas)

deposita_para_todas(contas)
print(conta_do_gui)
print(conta_da_dani)

# Uma lista, normalmente, possui objetos do mesmo tipo.

# Uma tupla, por contrário, possui objetos de tipos diferentes em que cada elemento possui uma representação.

#Para criarmos uma tupla, podemos utilizar o seguinte comando:

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

#As tuplas levam para o lado funcional, enquanto que as listas levam para uma abordagem orientada a objetos.

#Abaixo, estamos criando uma lista de tuplas.
usuarios = [guilherme, daniela]