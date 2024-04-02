saldo = 2000
limite_saque = 3

def sacar():
    global saldo
    global limite_saque
    valor_informado = round(float(input("Digite o valor que deseja sacar:\n")), 2)
    saque_maximo = 500

    if valor_informado > saque_maximo:
        saque_maximo_convertido = f"R${saque_maximo:.2f}".replace('.',',')
        print(f"Não é permitido sacar acima de R${saque_maximo_convertido}.")
    else:
        if valor_informado > saldo:
            print("Saldo Insuficiente!!!")
        else:
            if limite_saque <= 0:
                print("Você atingiu o limite de saques diário.")
            else:
                saldo -= valor_informado
                valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
                saldo_convertido = f"R${saldo:.2f}".replace('.',',')
                limite_saque -= 1
                print(f"Você sacou R${valor_convertido}, restam {saldo_convertido}.")

def depositar():
    global saldo
    valor_informado = round(float(input("Digite o valor que deseja depositar:\n")), 2)
    
    if valor_informado > 0:
        saldo += valor_informado
        valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
        saldo_convertido = f"R${saldo:.2f}".replace('.',',')
        print(f"Seu depósito de {valor_convertido} foi efetuado, seu saldo atual é {saldo_convertido}.")
    
    else:
        print("Deposite um valor válido.")

def consultar_saldo():
    global saldo
    saldo_convertido = f"R${saldo:.2f}".replace('.',',')
    print(f"Seu saldo atual é {saldo_convertido}")


def menu():
    while True:
        entrada = int(input("""

        #######################MENU#######################

                1. Sacar
                2. Depositar
                3. Consultar saldo
                0. Sair

        ##################################################

        """))
        if entrada == 0:
            print("Obrigada por usar nossos serviços.")
            break

        if entrada == 1:
            sacar()

        if entrada == 2:
            depositar()
        
        if entrada == 3:
            consultar_saldo()


print(menu())