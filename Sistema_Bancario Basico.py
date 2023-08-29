from time import sleep

menu = """
-----------Menu Principal -----------
            [d] - Depositar
            [s] - Sacar
            [e] - Extrato
            [q] - Sair
--------------------------------------
             """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = 0
valor_depositado = "" 
valor_sacado = ""

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        valor_deposito = float(input("Insira o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            depositos += 1
            valor_depositado += "|R$" + str(valor_deposito) + "| "
            print("Deposito realizado com sucesso")
            print ("voltando ao menu principal...")
            sleep(2)
        else:
            print("Valor inválido.")
            print ("voltando ao menu principal...")
            sleep(2)
    elif opcao.lower() == "s":
        valor_saque = float(input("Insira o valor a ser sacado: "))
        if valor_saque > 0:
            if numero_saques != LIMITE_SAQUES:
                if valor_saque <= limite:
                    if valor_saque <= saldo:
                        saldo -= valor_saque
                        numero_saques += 1
                        valor_sacado += "|R$" + str(valor_saque) + "| "
                        print("Valor sacado com sucesso.")
                        print ("voltando ao menu principal...")
                        sleep(2)
                    else: 
                        print ("Saldo insuficiente para sacar!")
                        print ("voltando ao menu principal...")
                        sleep(2)
                else:
                    print ("Você informado maior que o limite permitido.")
                    print ("voltando ao menu principal...")
                    sleep(2)
            else: 
                print ("Você chegou ao seu limite de saques.")
                print ("voltando ao menu principal...")
                sleep(2)
        else:
            print("Valor inválido.")
            print ("voltando ao menu principal...")
            sleep(2)

    elif opcao.lower() == "e":
        print(f"""
              ___________Extrato___________
              Saldo atual: R${saldo:.2f}
              
              Numero de depósitos: {depositos}
              Valores depositados: {valor_depositado}
              Numero de saques: {numero_saques}
              Valores sacados: {valor_sacado}\n""")
        print ("voltando ao menu principal...")
        sleep(2)
    elif opcao.lower() == "q":
        print("Obrigado por usar nosso sistema!")
        break
    else:
        print("opção inválida!")

