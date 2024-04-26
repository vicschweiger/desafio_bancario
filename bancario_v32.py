from datetime import datetime

class User:  
    users = []      
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.account = []
    
    @classmethod
    def show_info(cls, user):
        print(f"""
              {50 * '#'}
              
              ID: {user.id}")
              Nome: {user.name}
              Endereço: {user.address}
              Data de Nascimento: {user.birth_date}
              CPF: {user.cpf}
              Usuário: {user.username}")
            
              
              {50 * '#'}
              
              """)
        Transactions.operation_menu(user)
    
    @classmethod
    def name_request(cls):
        cls.name = input("\nDigite seu nome: ")
        return cls.name.title()
    
    @classmethod
    def bd_request(cls):
        while True:
    
            bd = input("\nDigite sua data de nascimento (AAAA-MM-DD): ")
            cls.birth_date =  datetime.strptime(bd, "%Y-%m-%d")
            current_year = datetime.now().year
            birth_year = cls.birth_date.year
            age = current_year - birth_year
            
            if age >= 18:
                return cls.birth_date

            else:
                print("\nVocê ainda não é maior de idade!")
                continue       
    
    @classmethod
    def address_request(cls):
        cls.address = input("\nDigite seu endereço: ")
        return cls.address.title()
    
    @classmethod
    def cpf_request(cls):
        cls.cpf = int(input("\nDigite seu CPF apenas número: "))
        return cls.cpf
    
    @classmethod
    def username_request(cls):
        cls.username = input("\nDigite seu nome de usuário: ")
        return cls.username
    
    @classmethod
    def password_request(cls):
        while True:
            min_length = 8
            capital_letter = False
            lowercase_letter = False
            one_number = False
            special_character = False

            cls.new_password = input("\nDigite a nova senha: ")
            
            if len(cls.new_password) < min_length:
                print(f"\nSua senha é muito curta. Recomenda-se pelo menos {min_length} caractéres.")
                continue

            for char in cls.new_password:
                if  char.isupper():
                    capital_letter = True
                elif char.islower():
                    lowercase_letter = True
                elif char.isdigit():
                    one_number = True
                elif not char.isalnum():
                    special_character = True

            common_sequences = ["123456", "abcdef"]
            for sequence in common_sequences:
                if sequence in cls.new_password:
                    print("Sua senha contém uma sequência comum. Tente uma senha mais complexa.")
                    continue

            common_words = ["password", "123456", "qwerty"]
            if cls.new_password in common_words:
                print("Sua senha contém uma sequência comum. Tente uma senha mais complexa.")
                continue
            elif not lowercase_letter:
                print("Sua senha precisa ter pelo menos uma letra minúscula.")
                continue
            elif not capital_letter:
                print("Sua senha precisa ter pelo menos uma letra maiúscula.")
                continue
            elif not one_number:
                print("Sua senha precisa ter pelo menos um número.")
                continue
            elif not special_character:
                print("Sua senha precisa ter pelo menos um caractere especial.")
                continue
            else:
                return cls.new_password
    
    @classmethod
    def get_next_id(cls):
        cls.next_id = len(cls.users) + 1
        return cls.next_id
    
    @classmethod
    def create_user(cls):
        name = cls.name_request()
        birth_date = cls.bd_request()
        address = cls.address_request()
        cpf = cls.cpf_request()
        username = cls.username_request()
        new_password = cls.password_request()
        next_id = cls.get_next_id()
        
        user1 = User(id=next_id, name=name, birth_date=birth_date, address=address, cpf=cpf, username=username, password=new_password)
        
        account1 = Account(id=next_id, number=1, branch="0001", balance=0, username=username)
        user1.account = account1  # Associa a conta ao usuário
        
        cls.users.append(user1)
        Account.accounts.append(account1)
        
    @classmethod
    def get_username(cls):
        cls.informed_username = input("\nDigite seu nome de usuário ou digite 0000 para sair: ")
        
        if cls.informed_username == "0000":
            main()
        else:
            for user in User.users:
                if user.username == cls.informed_username:
                    return True
    
    @classmethod
    def get_password(cls):
        cls.informed_password = input("\nDigite sua senha: ")
        for user in User.users:
            if user.password == cls.informed_password:
                return True
    
    # LOGIN - Checa nome de usuário e senha
    @classmethod
    def login(cls):
        while True:
            cls.get_username()
            cls.get_password()

            if cls.informed_username and cls.informed_username:
                for user in cls.users:
                    if user.username == cls.informed_username and user.password == cls.informed_password:
                        return Transactions.operation_menu(user)
                        
                print("\nUsuário ou senha inválidos!")
                continue
            else:
                print("\nUsuário ou senha inválidos!")
                continue
                
class Account(User): 
    
    accounts = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @classmethod   
    def show_balance(cls, user):
        
        cls.user = user
        
        formatted_balance = f"R${user.account.balance:.2f}".replace('.', ',')
        print(f"""
              {50 * '#'}
              
              Seu saldo atual é {formatted_balance}.
              
              {50 * '#'}
              
              """)
    
    # Método Sacar
    @classmethod
    def deposit(cls, user):
        
        cls.user = user
        
        while True:
            informed_value = int(input("\nDigite o valor que deseja depositar ou 0000 para voltar: "))
            
            if informed_value == 0000:
                Transactions.operation_menu(user)
                
            elif informed_value <= 0:
                print("\nDigite um valor válido!")
                continue
            
            else:
                user.account.balance = user.account.balance + informed_value
                
                formatted_value = f"R${informed_value:.2f}".replace('.', ',')
                formatted_balance = f"R${user.account.balance:.2f}".replace('.', ',')
                
                History.new_transaction(user.account, date=datetime.now(), 
                                        type="depósito", value=informed_value, 
                                        actual_balance=user.account.balance)
                
                print(f'\nVocê depositou {formatted_value}, seu saldo atual é {formatted_balance}.')
                continue
    
    # Método Depositar        
    @classmethod
    def withdraw(cls, user):
        
        cls.user = user
        
        while True:
            informed_value = int(input("\nDigite o valor que deseja sacar ou 0000 para voltar: "))
            
            if informed_value == 0000:
                Transactions.operation_menu(user)
                
            elif user.account.balance < informed_value:
                print("\nSaldo insuficiente.")
                continue
            
            else:
                user.account.balance = user.account.balance - informed_value
                    
                formatted_value = f"R${informed_value:.2f}".replace('.', ',')
                formatted_balance = f"R${user.account.balance:.2f}".replace('.', ',')
                
                History.new_transaction(user, date=datetime.now(), 
                                        type="saque", value=informed_value, 
                                        actual_balance=user.account.balance)
                
                print(f'\nVocê sacou {formatted_value}, seu saldo atual é {formatted_balance}.')
                continue       
    
class AdminAccount(Account):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def admin_menu(cls):
        while True:
            entry = input(f"""
                             {20 * '#'} MENU admin {20 * '#'}
                             
                                1. Mostrar todos usuários cadastrados
                                2. Mostrar todas contas cadastradas
                                0. Voltar
                                
                             {50 * '#'} 
                              """)
            
            match entry:
                
                # Volta ao Menu Principal
                case "0":
                    main()
                    
                # Mostra todos usuários cadastrados
                case "1":
                    AdminAccount.show_all_users()
                    
                # Mostra todos as contas cadastradas
                case "2":
                    AdminAccount.show_all_accounts()
                    
                case _:
                    print("Digite uma opção válida.")             
    
    # Método mostrar todos usuários
    @classmethod
    def show_all_users(cls):
        print("\nClientes cadastrados:")
        for user in cls.users:
            print(f"\nID: {user.id}")
            print(f"Nome: {user.name}")
            print(f"Data de Nascimento: {user.birth_date}")
            print(f"Endereço: {user.address}")
            print(f"CPF: {user.cpf}")
            print(f"Usuário: {user.username}")
            print(f'Senha: {user.password}')
            print(f'Saldo: {user.account.balance}')
    
    # Método mostrar todas contas
    @classmethod
    def show_all_accounts(cls):
        print("\nContas cadastradas:")
        for account in cls.accounts:
            print(f"\nID: {account.id}")
            print(f"Usuário: {account.username}")
            print(f'Saldo :{account.balance}')
              
class Transactions(Account):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @classmethod
    def operation_menu(cls, user):
        
        cls.user = user
        
        entry = input(f"""
                        {23 * '#'} MENU {23 * '#'}
                        
                            1. Depósito
                            2. Saque
                            3. Consultar Saldo
                            4. Extrato
                            0. Sair e Voltar
                            
                        {50 * '#'} 
                        """)
        match entry:
            
            # Volta ao menu anterior
            case "0":
                main()
            
            # Função Depósito
            case "1":
                Account.deposit(user)
                
            # Função Saque
            case "2":
                Account.withdraw(user)
                
            #  Função mostrar saldo               
            case "3":
                Account.show_balance(user)
            
            # Função Extrato
            case "4":
                History.show_transactions(user)
            
            # Mostra Informações do usuário
            case "5":
                User.show_info(user)
                
            # Demais casos
            case _:
                print("\nOpção inválida, por favor digite uma opção válida!")

class History(Transactions):
    
    transactions = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @classmethod
    def new_transaction(cls, user, **kwargs):
        new_transaction = {
            'account_id': user.id,
            'date': kwargs.get('date'),
            'type': kwargs.get('type'),
            'value': kwargs.get('value'),
            'actual_balance': kwargs.get('actual_balance')
        }
        
        cls.transactions.append(new_transaction)  
        
    @classmethod
    def show_transactions(cls, user):
        print(f"\nConta: {user.account.id}")
        print(f"\nSaldo: {user.account.balance:.2f}".replace('.', ','))
        print(f"\n{50 * "#"}\n")
        print("""   DATA    |   HORA    |       Operação        |   Valor   |   Saldo   """)
              
        for transaction in cls.transactions:
            
            formatted_value = f"R${transaction['value']:.2f}".replace('.', ',')
            formatted_balance = f"R${transaction['actual_balance']:.2f}".replace('.', ',')
            print(f"{transaction['date']} | {transaction['type'].capitalize()} | {formatted_value} | {formatted_balance}")
            
        print(f"\n{50 * "#"}\n")
        return Transactions.operation_menu(user)
            
        

# Menu Principal      
def main():
    while True:
        entrada = input(f"""
            {23 * '#'} MENU {23 * '#'}
            
            1. Criar conta
            2. Login
            3. Admin
            0. Sair
                
            {50 * '#'}          
            """)
        
        match entrada:
            
            # Finaliza Programa
            case "0":
                print("\nObrigada por usar nossos serviços, volte sempre!")
                break
            
            # Menu Criar Usuário e Conta
            case "1":
                User.create_user()
                
            # Menu Login
            case "2":
                User.login()
            
            #  Menu Admin 
            case "3":
                AdminAccount.admin_menu()
                
            # Demais Casos
            case _:
                print("\nOpção inválida, por favor digite uma opção válida!")
                continue
            
if __name__ == "__main__":
    main()
