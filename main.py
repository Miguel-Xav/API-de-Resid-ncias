#módulos de fora
import time
#meu módulo para comunicar com o sqlite
import commsqlite3
#módulo separado com funções para cadastrar uma residência
import funcad

def menu_principal():
    commsqlite3.criar_tabela()
    print ("Seja bem vindo a interface que vai te ajudar a controlar seu apartamento")
    list_op = ['Criar uma residência', 'Editar uma residência', 'Excluir uma residência', 'Listar', 'Sair']

    while True:
        time.sleep(2)
        print ("Você deseja realizar qual operação?")
        time.sleep(1)
        for indice, item in enumerate(list_op, start=1):
            print (f'{indice}. {item}')
        print ('Para voltar ao menu principal no meio de qualquer operação, digite "sair"')
        escolha = input(": ")


        if escolha == '1':
            nome_cad = funcad.obt_nome_res()
            if nome_cad is None:
                print ("Operação cancelada. Voltando ao menu principal...")
                time.sleep (2)
                continue
            else:
                endereco_cad = funcad.obt_end_res()
                if endereco_cad is None:
                        print ("Operação cancelada. Voltando ao menu principal...")
                        time.sleep (2)
                        continue
                else:
                        cep_cad = funcad.obt_cep_res()
                        if cep_cad is None:
                            print ("Operação cancelada. Voltando ao menu principal...")
                            time.sleep (2)
                            continue
                        else:
                            id_nova_res = commsqlite3.adicionar_res(nome_cad, endereco_cad, cep_cad)
                            print (f"Residência cadastrada com sucesso! \nNome: {nome_cad}\nEndereço: {endereco_cad}\nCEP: {cep_cad}\nID da residência: {id_nova_res}\nVoltando ao menu principal")
                            time.sleep(4)
        elif escolha == '2':
            id_res = input('Digite o ID da residência que você deseja editar: ')
            if id_res.lower() == 'sair':
                print ("Operação cancelada, voltando ao menu principal...")
                time.sleep (2)
                continue
            dados_res = commsqlite3.listar_res()
            residencia = next((r for r in dados_res if r[0] == int(id_res)), None)

            if residencia:
                novo_nome = funcad.obt_nome_res() or residencia[1]
                novo_endereco = funcad.obt_end_res() or residencia[2]
                novo_cep = funcad.obt_cep_res() or residencia[3]

                commsqlite3.edit_res(residencia[0], novo_nome, novo_endereco, novo_cep)
                print ('Residência atualizada com sucesso!')
            else:
                print ("Residência não econtrada")
        elif escolha == '3':
            while True:
                escolha_exc = input("Qual ID da residência que você quer excluir?: ")
                if escolha_exc.lower() == 'sair':
                    print ("Operação cancelada, voltando ao menu principal...")
                    time.sleep (2)
                    break
                elif escolha_exc.isdigit():
                    escolha_exc = int(escolha_exc)
                    residencia = commsqlite3.listar_res()
                    ids_existentes = [residencia[0]for residencia in residencia]
                    
                    if escolha_exc in ids_existentes:
                        commsqlite3.deletar_res(escolha_exc)
                        
                        residencia_atualizadas = commsqlite3.listar_res()
                        ids_atualizadas = [residencia[0]for residencia in residencia_atualizadas]
                        
                        if escolha_exc not in ids_atualizadas:
                            print ("Operação concluida com sucesso! Voltando ao menu principal")
                            time.sleep(3)
                            break
                        else:
                            print ("Falha na operação, tente novamente")
                            break
                    elif escolha_exc not in ids_existentes:
                        ("ID não encontrado, tente novamente")
                        time.sleep(2)
                else:
                    print ("ID inválido, tente novamente")
        elif escolha == '4':
            residencias = commsqlite3.listar_res()
            if not residencias:
                print ("Não há residências cadastradas, voltando ao menu principal...")
            else:
             for residencia in residencias:
                 print (f"ID: {residencia[0]},Nome: {residencia[1]},Endereço: {residencia[2]},CEP: {residencia[3]}")
        elif escolha == '5':
            print ("Saindo...")
            time.sleep(3)
            break               
        else:
            print("Digite uma opção válida")

menu_principal()