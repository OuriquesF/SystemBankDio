#SISTEMA BANCARIO COM AS SEGUINTES OPÇÕES
menu = """

####### BEM VINDO A DIOBANK #######

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

###################################

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("############# DIOBANK #############\n\n\nVocê selecionou a opção de deposito!\nQual valor deseja depositar?\n"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"\nVocê depositou R$ {valor:.2f}\n")
        else:
            print("OPERAÇÃO INVALIDADE!")
    elif opcao == "2":
        valor = float(input("############# DIOBANK #############\n\n\nVocê selecionou a opção de saque!\nQual valor deseja sacar?\n"))   

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
                print("Você não possui saldo suficiente para esta operação!""")    

        elif excedeu_limite:
                print("Você execedeu o valor limite para seus saques diarios!""")

        elif excedeu_saques:
                print("Você excedeu o limite de saques diarios!")

        elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque efetuado com sucesso!\nValor do saque R$ {valor:.2f}")

        else:
                print("Valor informado invalido!")
    elif opcao == "3":
        print("############# DIOBANK #############\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")
    elif opcao == "0":
        print("Volte sempre ao DIOBANK!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")