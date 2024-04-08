from datetime import datetime

data_atual = datetime.now()
data_atual_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")

# FUNÇÃO ADICIONAR TRANSAÇÃO

extrato = []

def adicionar_transacao(data_atual_formatada, operação, valor_convertido):
    global extrato
    nova_transacao = {
        "data": data_atual_formatada,
        "tipo de operacao": operação,
        "valor": valor_convertido
    }
    extrato.append(nova_transacao)

# FUNÇÃO EXTRATO

def mostra_extrato(extrato):

    if len(extrato) > 0:
        print("Essas são as últimas transações:")
        for transacao in extrato:
            print(f"{transacao['data']} - {transacao['tipo de operacao'].capitalize()} - {transacao['valor']}")

        entrada = int(input(f"""
        
        Digite 0 para voltar ao menu anterior
                            
        """))
                                
        if entrada == 0:
            menu_operacao()
    else:
        print("Essa conta não possui transações recentes.")
        menu_operacao()

# FUNÇÃO SACAR

limite_saque = 3

def sacar():
    global clientes
    global limite_saque
    global data_atual_formatada
    operacao = "saque"
    saldo = clientes["usuario"]["saldo"]
    valor_informado = round(float(input("Digite o valor que deseja sacar:\n")), 2)
    saque_maximo = 500

    # Verifica limite de saque diário

    if limite_saque <= 0:
        print("Você atingiu o limite de saques diário.")
    else:

    # Verifica saldo

        if valor_informado > saldo:
            print("Saldo Insuficiente!!!")
        else:

            # Verifica valor de saque máximo

            if valor_informado > saque_maximo:
                saque_maximo_convertido = f"R${saque_maximo:.2f}".replace('.',',')
                print(f"Não é permitido sacar acima de {saque_maximo_convertido}.")
            else:
                saldo -= valor_informado
                valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
                saldo_convertido = f"R${saldo:.2f}".replace('.',',')
                limite_saque -= 1
                print(f"Você sacou R${valor_convertido}, restam {saldo_convertido}.")
                adicionar_transacao(data_atual_formatada, operacao, valor_convertido)

# FUNÇÃO DEPOSITAR

def depositar():
    global clientes
    global data_atual_formatada
    operacao = "depósito"
    valor_informado = round(float(input("Digite o valor que deseja depositar:\n")), 2)
    
    # Verifica se valor é positivo

    if valor_informado > 0:
        saldo = clientes["usuario"]["saldo"]
        saldo += valor_informado
        clientes["usuario"]["saldo"] = saldo
        valor_convertido = f"R${valor_informado:.2f}".replace('.',',')
        saldo_convertido = f"R${saldo:.2f}".replace('.',',')
        print(f"Seu depósito de {valor_convertido} foi efetuado, seu saldo atual é {saldo_convertido}.")
        adicionar_transacao(data_atual_formatada, operacao, valor_convertido)
    
    else:
        print("Deposite um valor válido.")

# FUNÇÃO CONSULTAR SALDO

def consultar_saldo():
    global clientes
    saldo = clientes["usuario"]["saldo"]
    saldo_convertido = f"R${saldo:.2f}".replace('.',',')
    print(f"Seu saldo atual é {saldo_convertido}")

# FUNÇÃO VALIDA SENHA

def verificar_forca_senha():
    global clientes
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    nova_senha = input("Digite a nova senha:\n").strip()

    while True:
        if len(nova_senha) < comprimento_minimo:
            print(f"Sua senha é muito curta. Recomenda-se pelo menos {comprimento_minimo} caracteres.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue

        for char in nova_senha:
            if  char.isupper():
                tem_letra_maiuscula = True
            elif char.islower():
                tem_letra_minuscula = True
            elif char.isdigit():
                tem_numero = True
            elif not char.isalnum():
                tem_caractere_especial = True

        sequencias_comuns = ["123456", "abcdef"]
        for sequencia in sequencias_comuns:
            if sequencia in nova_senha:
                print("Sua senha contém uma sequência comum. Tente uma senha mais complexa.")
                nova_senha = input("Digite a senha novamente:\n").strip()
                continue

        palavras_comuns = ["password", "123456", "qwerty"]
        if nova_senha in palavras_comuns:
            print("Sua senha contém uma sequência comum. Tente uma senha mais complexa.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue
        elif not tem_letra_minuscula:
            print("Sua senha precisa ter pelo menos uma letra minúscula.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue
        elif not tem_letra_maiuscula:
            print("Sua senha precisa ter pelo menos uma letra maiúscula.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue
        elif not tem_numero:
            print("Sua senha precisa ter pelo menos um número.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue
        elif not tem_caractere_especial:
            print("Sua senha precisa ter pelo menos um caractere especial.")
            nova_senha = input("Digite a senha novamente:\n").strip()
            continue
        else:
            clientes["usuario"]["senha"] = nova_senha
            break


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
    
    # Volta ao menu inicial (anterior)
    
    if entrada == 0:
        print(menu_inicial())

    # Verifica login e senha

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
        "cpf": "",
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
    
    # Volta ao menu inicial (anterior)
    
    if entrada == 0:
        menu_inicial()

    # Cadastra novo cliente

    elif entrada == 1:

        global clientes
        
        # Verifica se nome de usuário já existe

        nome_de_usuario = str(input("Digite o nome de usuário:\n"))

        for cliente_info in clientes.values():
            if cliente_info.get("nome_de_usuario") == nome_de_usuario:
                print("Nome de usuário já cadastrado.")
                return menu_criar_conta() 

            else:
                nome_de_usuario = clientes["usuario"]["nome_de_usuario"]
                clientes["usuario"]["nome_de_usuario"] = nome_de_usuario

                # Verifica maioridade

                idade = int(input("Digite sua idade:\n"))

                if idade >= 18:
                    clientes["usuario"]["idade"] = idade

                    # Verifica CPF

                    cpf = str(input("Digite seu CPF, somente números:\n"))

                    for clientes_info in clientes.values():
                        if clientes.get("cpf") == cpf:
                            print("Esse CPF já esta cadastrado.")
                            cpf = str(input("Digite seu CPF, somente números:\n"))

                        else:
                            clientes["usuario"]["cpf"] = cpf
                            clientes["usuario"]["nome"] = str(input("Digite seu nome completo:\n"))
                            clientes["usuario"]["endereco"]["rua"] = str(input("Digite o logradouro:\n"))
                            clientes["usuario"]["endereco"]["numero"] = int(input("Digite o número:\n"))
                            clientes["usuario"]["endereco"]["bairro"] = str(input("Digite o bairro:\n"))
                            clientes["usuario"]["endereco"]["cidade"] = str(input("Digite a cidade:\n"))
                            clientes["usuario"]["endereco"]["estado"] = str(input("Digite o estado:\n"))

                            # Gera Id, número de conta e saldo

                            numero_de_clientes = len(clientes) - 1
                            id_da_conta = numero_de_clientes + 1
                            numero_da_conta = "{:04d}".format(id_da_conta)

                            clientes["usuario"]["id_da_conta"] = id_da_conta
                            clientes["usuario"]["numero_da_conta"] = numero_da_conta
                            clientes["usuario"]["saldo"] = 0
                            print(verificar_forca_senha())

                            print(menu_login())

                else:
                    print("Você ainda não é maior de idade!")
                    print(menu_inicial())


# MENU OPERAÇÕES

def menu_operacao():
    while True:
        entrada = int(input(f"""

        #######################MENU#######################
                            
            Olá, {clientes['usuario']['nome']},
            qual operação deseja realizar hoje?

                1. Sacar
                2. Depositar
                3. Consultar saldo
                4. Extrato
                0. Sair

        ##################################################

        """))
        if entrada == 0:
            print(f"Obrigada por usar nossos serviços, {clientes['usuario']['nome']}. Volte sempre!")
            print(menu_inicial())
            break

        elif entrada == 1:
            sacar()

        elif entrada == 2:
            depositar()
        
        elif entrada == 3:
            consultar_saldo()
        
        elif entrada == 4:
            mostra_extrato(extrato)

menu_inicial()