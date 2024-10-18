#funções para realizar o cadastro
def obt_nome_res():
        while True:
            nome = input('Digite o nome da residência: ').strip()
            if nome.lower() == "sair":
                return None
            elif nome:
                 return nome
            else:
                 print ("Nome inválido, tente novamente")

def obt_end_res():
        while True:
            endereco = input("Digite o endereço: ").strip()
            if endereco.lower() == 'sair':
                 return None
            elif endereco:
                 return endereco
            else:
                print ("Endereço inválido, tente novamente")

def obt_cep_res():
        while True:
            cep = (input("Digite o cep (apenas os números): ")).strip()
            if cep.lower() == 'sair':
                 return None
            elif len(cep) == 8 and cep.isdigit():
                return cep
            else:
                print ("CEP inválido, 8 dígitos de apenas números, tente novamente")