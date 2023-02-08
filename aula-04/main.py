# O "==", por padrão, verifica o endereço de memória dos objetos. Para sobrescrevermos a comparação, devemos
# sobrescrever o método "__eq__".

class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        return self._codigo == outro._codigo


# O método "isInstance(objeto, objeto) verifica se um objeto é do tipo de outro objeto, ou é de um subtipo desse objeto.

