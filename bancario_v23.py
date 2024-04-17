from datetime import datetime

class Cliente:
    def __init__(self, nome, endereco, senha):
        self.nome = nome
        self.endereco = endereco
        self.senha = senha
        self.contas = []
        prox_numero = len(self.contas)

    def realizar_transacao(self, conta, transacao):
        pass
    
    @classmethod
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, data_nascimento):
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta(Cliente):
    def __init__(self, numero, cliente, historico):
        self.saldo = 0
        self.numero = numero
        self.cliente = cliente
        self.historico = historico
        self.agencia = "0001"
    
    @property
    def saldo(self):
        return f"R$ {self.saldo:.2f}".replace('.',',')
    
    @property 
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def mostra_valor(self, valor):
        print(f"R${valor:.2f}".replace('.',','))
    
    def consultar_saldo(self):
        print(f"Seu saldo atual é {self.mostra_valor(self.saldo)}.")

    def sacar(self, valor_informado):
        self.valor_informado = valor_informado

        if valor_informado > self.saldo:
            print("Não foi possível realizar o saque, saldo insuficiente!")
        else:
            self.saldo = self.saldo - valor_informado
            print(f"Você sacou {self.mostra_valor(valor_informado)}, seu saldo é {self.mostra_valor(self.saldo)}.")
            self.historico.registrar_transacao(valor_informado, self.saldo, tipo="saque")

    def depositar(self, valor_informado):
        self.valor_informado = valor_informado

        if valor_informado > 0:
            self.saldo += valor_informado
            print(f"Você depositou {self.mostra_valor(valor_informado)}, seu saldo é {self.mostra_valor(self.saldo)}.")
            self.historico.registrar_transacao(valor_informado, self.saldo, tipo="depósito")
        else:
            print("Digite um valor positivo.")

class Historico(Conta):
    def __init__(self, valor_informado, tipo, saldo):
        super().__init__(valor_informado, tipo, saldo)
        self.transacoes = []

    def registrar_transacao(self, tipo, saldo, valor_informado):
        self.saldo = saldo
        transacao = {'data': datetime.now().strftime("%d-%m-%Y %H:%M:%s"), 'tipo': tipo, 'valor': valor_informado,  'saldo': saldo}
        return transacao
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
    
    def exibir_extrato(self, transacoes):
        print("Data       | Tipo     | Valor    | Saldo")
        print("-----------------------------------------")
        for transacao in transacoes:
            data = transacao['data']
            tipo = transacao['tipo']
            valor = transacao['valor_informado']
            saldo = transacao['saldo']
            print(f"{data} | {tipo.capitalize()} | {self.mostra_valor(valor)} | {self.mostra_valor(valor)}")
            print("-----------------------------------------")

def main():
    while True:
        entrada = int(input("""

            #######################MENU#######################
                                
                1. Login
                2. Criar conta
                0. Sair
                                    
            ##################################################


            """))
        
        match entrada:

            case 0:
               print("Obrigada por usar nossos serviços, volte sempre!")
               break

            case 1:
                pass

            case 2:
                criar_conta()

            case _:
                print("Opção Inválida")

def criar_conta():
    nome = input("Digite seu nome:\n")
    data_informada = input("Digite sua data de nascimento (AAAA-MM-DD):\n")
    data_nascimento =  datetime.strptime(data_informada, "%Y-%m-%d")
    ano_atual = datetime.now().year
    ano_nascimento = data_nascimento.year
    idade = ano_atual - ano_nascimento
    endereco = str(input("Digite seu endereço:\n"))
    cpf = input("Digite seu CPF:\n")
    senha = input("Digite sua senha sendo 1 caractére maiúsculo, 1 minúsculo, 1 número e 1 caractére especial:\n")

    conta = Cliente(nome=nome,endereco=endereco, senha=senha)
    Cliente.adicionar_conta(conta)

    print("Conta criada com sucesso!")
    print(f"Nome do titular: {Cliente.nome}")
    print(f"Número da conta: {Conta.numero}")
    print(f"Saldo inicial: R${Conta.saldo:.2f}")

main()