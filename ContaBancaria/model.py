class Pessoa:
    def __init__(self, cpf, nome, endereco, telefone):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


class Conta:
    def __init__(self, Pessoa, senha, numero, saldo):
        self.pessoa = Pessoa
        self.senha = senha
        self.numero = numero
        self.saldo = saldo


    def getSaldo(self):
        return self.saldo


    def getNumero(self):
        return self.numero


    def getSenha(self):
        return self.senha

    def consult(self):
        return self.pessoa, self.senha, self.numero


    def sacar(self, valor):
        restante = self.getsaldo() - valor
        if restante > 0:
            self.saldo = restante
            return True
        return False


    def depositar(self, valor):
        self.saldo += valor
