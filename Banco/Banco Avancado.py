import textwrap ## SÓ PERFUMARIA


def menu():
    menu = """\n
    
    ================== MENU ===================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    
    ===>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito R$ {valor: .2f}\n"
        print("\n=== Depósito realizado com Sucesso! ===")

    else:
        print("\n@@@ A operação falhou! O valor informado é inválido! @@@")

    return saldo, extrato

def main ():


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do Deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do Saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saques >= limite_saques

            if excedeu_saldo:
                print("Operação Falhou! Você não tem saldo suficiente")
            elif excedeu_limite:
                print("Operação Falhou! O valor do saque excede o limite")
            elif excedeu_saque:
                print("Operação Falhou! Número Máximo de saques excedido")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: .2f}\n"
                numero_saques += 1

            else:
                print("Operação Falhou! O valor informado é inválido!")

        elif opcao == "e":
            print("\n ########################### EXTRATO ##########################")
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo: .2f}")
            print("###########################################################")

        elif opcao == "q":
            print("Obrigado por utilizar nosso serviços, o Banco Luna agradece!")
            break


        else:
            print("Operação Inválida, por favor selecione novamente a operação desejada")