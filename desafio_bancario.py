# FUNÇÃO SACAR

limite_saque = 3

def sacar():
    global clientes
    global limite_saque
    saldo = clientes["usuario"]["saldo"]
    valor_informado = round(float(input("Digite o valor que deseja sacar:\n")), 2)
    saque_maximo = 500

    # Verifica valor de saque máximo

    if valor_informado > saque_maximo:
        saque_maximo_convertido = f"R${saque_maximo:.2f}".replace('.',',')
        print(f"Não é permitido sacar acima de R${saque_maximo_convertido}.")
    else:

        # Verifica saldo

        if valor_informado > saldo:
            print("Saldo Insuficiente!!!")
        else:

            # Verifica limite de saque diário

            if limite_saque <= 0:
                print("Você atingiu o limite de saques diário.")
            else:
                saldo -= valor_informado
                valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
                saldo_convertido = f"R${saldo:.2f}".replace('.',',')
                limite_saque -= 1
                print(f"Você sacou R${valor_convertido}, restam {saldo_convertido}.")

# FUNÇÃO DEPOSITAR

def depositar():
    global clientes
    valor_informado = round(float(input("Digite o valor que deseja depositar:\n")), 2)
    
    # Verifica se valor é positivo

    if valor_informado > 0:
        saldo = clientes["usuario"]["saldo"]
        saldo += valor_informado
        clientes["usuario"]["saldo"] = saldo
        valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
        saldo_convertido = f"R${saldo:.2f}".replace('.',',')
        print(f"Seu depósito de {valor_convertido} foi efetuado, seu saldo atual é {saldo_convertido}.")
    
    else:
        print("Deposite um valor válido.")

# FUNÇÃO CONSULTAR SALDO

def consultar_saldo():
    global clientes
    saldo = clientes["usuario"]["saldo"]
    saldo_convertido = f"R${saldo:.2f}".replace('.',',')
    print(f"Seu saldo atual é {saldo_convertido}")

# MENU INICIAL

def menu_inicial():
    while True:
        entrada = int(input("""

        #######################MENU#######################
                            
            1. Login
            2. Criar conta
            0. Sair
                                
        ##################################################


        """))
        if entrada == 0:
            print("Obrigada por usar nosso serviços, volte sempre!")
            break
        elif entrada == 1:
            print(menu_login())
        elif entrada == 2:
            print(menu_criar_conta())

# MENU LOGIN

def menu_login():
    entrada = int(input("""

    1. Login
    0. Voltar

"""))
    
    if entrada == 0:
        print(menu_inicial())

    elif entrada == 1:
        global clientes
        usuario_informado = str(input("Digite seu usuário:\n"))
        senha_informada = str(input("Digite sua senha:\n"))
        usuario_correto = clientes["usuario"]["nome_de_usuario"]
        senha_correta = clientes["usuario"]["senha"]

        if usuario_informado == usuario_correto and senha_informada == senha_correta:
            print(menu_operacao())
        else:
            print("Nome de usuário ou senha incorretos!")
            print("Tente novamente!")
            print(menu_login())

# DICIONÁRIO CLIENTES

clientes = {
    "usuario": {
        "id_da_conta": "",
        "numero_da_conta": "",
        "saldo": 0,
        "nome": "",
        "idade": "",
        "endereco": {
            "rua": "",
            "numero": "",
            "bairro": "",
            "cidade": "",
            "estado": ""
        },
        "nome_de_usuario": "",
        "senha": ""
    }
}

# MENU CRIAR CONTA

def menu_criar_conta():
    entrada = int(input("""

    1. Criar novo usuário e conta.
    0. Voltar

"""))
    
    if entrada == 0:
        print(menu_inicial())

    elif entrada == 1:

        global clientes
        nome = str(input("Digite seu nome completo:\n"))
        idade = int(input("Digite sua idade:\n"))

        # Verifica maioridade

        if idade >= 18: 
            clientes["usuario"]["nome"] = nome
            clientes["usuario"]["idade"] = idade
            clientes["usuario"]["endereco"]["rua"] = str(input("Digite o logradouro:\n"))
            clientes["usuario"]["endereco"]["numero"] = int(input("Digite o número:\n"))
            clientes["usuario"]["endereco"]["bairro"] = str(input("Digite o bairro:\n"))
            clientes["usuario"]["endereco"]["cidade"] = str(input("Digite a cidade:\n"))
            clientes["usuario"]["endereco"]["estado"] = str(input("Digite o estado:\n"))
            clientes["usuario"]["nome_de_usuario"] = input("Digite o nome de usuário:\n")
            clientes["usuario"]["senha"] = input("Digite a senha:\n")
            clientes["usuario"]["saldo"] = 0

            # Gera Id e número de conta

            numero_de_clientes = len(clientes) - 1
            id_da_conta = numero_de_clientes + 1
            numero_da_conta = "{:04d}".format(id_da_conta)

            clientes["usuario"]["id_da_conta"] = id_da_conta
            clientes["usuario"]["numero_da_conta"] = numero_da_conta

            print(menu_login())

        else:
            print("Você ainda não é maior de idade!")
            print(menu_inicial())


# MENU OPERAÇÕES

def menu_operacao():
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
            print(menu_inicial())
            break

        elif entrada == 1:
            sacar()

        elif entrada == 2:
            depositar()
        
        elif entrada == 3:
            consultar_saldo()


print(menu_inicial())