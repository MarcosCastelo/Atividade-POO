from controller import *

def menu(state):
    string = ""
    if state == 1:
        string = "Digite a opçao de operaçao\n" \
                 "1 - Acessar Conta\n" \
                 "2 - Depoistar Saldo\n" \
                 "3 - Criar Conta\n" \
                 "0 - Sair\n"
    elif state == 2:
        string = "Digite a opçao de operaçao\n" \
                 "1 - Exibir Extrato\n" \
                 "2 - Realizar Saque\n" \
                 "3 - Realizar Transferencia\n" \
                 "0 - Sair"
    print(string)




def main():
    caixa = Caixa(None)
    logged = None
    print("\t\tBem vindo ao MarBank")
    menu(1)
    while True:
        op = input()
        if logged is None:
            if op == 1:
                pass
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 0:
                break
            else:
                print("Digite uma operacao valida")
            menu(1)
        else:
            if op == 1:
                pass
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 0:
                break
            else:
                print("Digite uma operacao valida")
            menu(2)





if __name__ == '__main__':
    main()