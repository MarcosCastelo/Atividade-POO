from model import *

class Caixa:
    def __init__(self, contas):
        self.contas = contas
        self.sessao = None


    def buscarConta(self, numero):
        for conta in self.contas:
            if conta.getNumero() == numero:
                return conta

        return None


    def depositar(self, numero, valor):
        conta = self.buscarConta(numero)
        conta.depositar(valor)


    def login(self, numero, senha):
        conta = self.buscarConta()
        if conta is not None and conta.getSenha() == senha:
            self.sessao = conta


    def isLogged(self):
        if self.sessao is not None:
            return True
        return False


    def logout(self):
        self.sessao = None


    def sacar(self, conta, valor):
        if self.isLogged():
            if self.sessao.sacar(valor):
                return True
            return False
        return False


    def consult(self, conta):
        if self.isLogged():
            return self.sessao.consult()
        return False


    def criarConta(self, cpf, nome, endereco, telefone, senha, numero, saldo):
        try:
            pessoa = Pessoa(cpf, nome, endereco, telefone)
            conta = Conta(pessoa, senha, numero, saldo)
            self.contas.append(conta)
        except:
            return False


