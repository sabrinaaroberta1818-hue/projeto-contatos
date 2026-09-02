import os
os.system("cls")

import sys

contatos = ({
    "MARIANA ALVES": "98888-5555",
    "ANA DUARTE": "97777-2222",
    "LUCAS HENRIQUE": "99999-7777",
    "GABRIEL SOUZA": "991111-8888",
    "ISABELA MARTINS": "96666-1111",
    "RAFAEL OLIVEIRA": "92222-4444",
    "CAMILA FERREIRA": "93333-6666",
    "PEDRO AUGUSTO": "95555-2222",
    "LARISSA COSTA": "98888-3333",
    "JOÃO VICTOR": "91111-2222",
    "BEATRIZ CARVALHO": "90000-7777",
    "MATHEUS ROCHA": "90000-5555",
    "SOFIA MENDES": "99999-6666",
    "DANIEL RIBEIRO": "9000-1111",
    "JULIANA BARROS": "94444-0000"
})

def menu():
    print("Bem-vindo(a) ao Portal de Operações! 🤩")
    print("Veja as opções de execução disponíveis:")
    print("1 - Adicionar contato ➕")
    print("2 - Pesquisar contato 🔍")
    print("3 - Editar contato ✏️")
    print("4 - Excluir contato ❌")
    print("5 - Mostrar todos os contatos 📋")
    print("6 - Sair do programa 🚪")
    print("")

def reapresentar_menu():
    while True:
            print("")
            pergunta = input("Gostaria de realizar outra operação? Digite 'sim' para continuar ou qualquer outra tecla para sair: ")
            if pergunta.upper() == "SIM":
                print("")
                print("Veja as opções de execução disponíveis:")
                print("1 - Adicionar contato ➕")
                print("2 - Pesquisar contato 🔍")
                print("3 - Editar contato ✏️")
                print("4 - Excluir contato ❌")
                print("5 - Mostrar todos os contatos 📋")
                print("6 - Sair do programa 🚪")
                print("")
                fluxo_logistico()
            else:
                sair_programa()

def obter_opcao():
    while True:
        try:
            escolha = int(input("Selecione a execução desejada de acordo com seu número correspondente: "))
            if escolha in [1, 2, 3, 4, 5, 6]:
                return escolha
            else:
                print("Opção inexistente. Por favor, selecione uma das opções apresentadas.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, selecione uma das opções apresentadas.")
            continue

def normalizar_nome(nome):
    return " ".join(nome.strip().upper().split())

def normalizar_numero(numero):
    return "".join(char for char in numero if char.isdigit())

def pesquisar_contato():
    while True:
        print("")
        busca_tipo = input("Gostaria de procurar por nome ou por número? ").strip().upper()
        if busca_tipo in ["NOME", "POR NOME"]:
            print("")
            busca = normalizar_nome(input("Qual contato deseja encontrar? "))
            encontrado = False
            for nome, numero in contatos.items():
                if normalizar_nome(nome) == busca:
                    print("")
                    print(f"Aqui está --> {nome} : {numero}.")
                    encontrado = True
                    break
            if not encontrado:
                print("")
                print("Contato não encontrado.")
            break
        elif busca_tipo in ["NÚMERO", "NUMERO", "POR NÚMERO", "POR NUMERO"]:
            busca_2 = normalizar_numero(input("Qual número deseja encontrar? "))
            encontrado = False
            for nome, numero in contatos.items():
                if normalizar_numero(numero) == busca_2:
                    print("")
                    print(f"Aqui está --> {nome} : {numero}.")
                    encontrado = True
                    break
            if not encontrado:
                print("")
                print("Contato não encontrado.")
            break
        else:
            print("")
            print("Não existe tal opção. Por favor, escolha entre nome ou número.")

def adicionar_contato():
    while True:
        print("")
        adicao_nome = normalizar_nome(input("Informe o nome do contato para adicionar: "))
        adicao_numero = normalizar_numero(input("Informe o número do contato para adicionar: "))
        if not adicao_nome:
            print("")
            print("O nome não pode ficar vazio.")
            continue
        if not adicao_numero:
            print("")
            print("O número não pode ficar vazio.")
            continue
        if adicao_nome in contatos:
            print("")
            print("Já existe um contato com esse nome. Informe um outro nome para adicionar:")
            continue
        if adicao_numero in contatos.values():
            print("")
            print("Já existe um contato com esse número. Informe um outro número para adicionar:")
            continue
        print("")
        confirmar = input(f"Por favor confirme o contato: {adicao_nome} : {adicao_numero}. Digite 'sim' para confirmar: ")
        if confirmar.upper() == "SIM":
            contatos[adicao_nome] = adicao_numero
            print("")
            print(f"Pronto! O contato {adicao_nome} foi adicionado à lista de contatos.")
            break
        elif confirmar.upper() == "NÃO" or confirmar.upper() == "NAO":
            print("")   
            print("Contato não confirmado. As informações serão solicitadas novamente.")
        else:
            print("")
            print("Resposta inválida. Digite 'sim' ou 'não'.")
            continue

def excluir_contato():
    while True:
        print("")
        excluir = normalizar_nome(input("Qual contato deseja excluir? "))
        if excluir in contatos:
            del contatos[excluir]
            print("")
            print(f"O contato {excluir} foi excluído com sucesso!")
            break
        else:
            print("")
            print("Contato não encontrado.")
            continue
    
def mostrar_contatos():
    print("")
    print("Aqui estão todos os contatos disponíveis:")
    for nome, numero in contatos.items():
        print(f"{nome} : {numero}")

def editar_contato():
    while True:
        print("")
        editar = normalizar_nome(input("Qual contato deseja editar? "))
        if editar in contatos:
            print("")
            nome_editado = normalizar_nome(input("Informe o novo nome do contato: "))
            numero_editado = normalizar_numero(input("Informe o novo número do contato: "))
            if not nome_editado:
                print("")
                print("O nome não pode ficar vazio.")
                continue
            elif not numero_editado:
                print("")
                print("O número não pode ficar vazio.")
                continue
            elif nome_editado in contatos and nome_editado != editar:
                print("")
                print("Já existe outro contato com esse nome.")
                continue
            elif numero_editado in contatos.values() and numero_editado != contatos[editar]:
                print("")
                print("Já existe outro contato com esse número.")
                continue
            if nome_editado == editar:
                contatos[editar] = numero_editado
            else:
                contatos[nome_editado] = numero_editado
                del contatos[editar]
                print("")
                print(f"O contato {editar} foi editado para {nome_editado} : {numero_editado}.")
                break
        else:
            print("")
            print("Contato não encontrado.")
            continue

def sair_programa():
    print("")
    print("Obrigado por utilizar o Portal de Operações! Até a próxima ✌🏻.")
    exit()

def fluxo_logistico():
        escolha = obter_opcao()
        if escolha == 1:
            adicionar_contato()
        elif escolha == 2:
            pesquisar_contato()
        elif escolha == 3:
            editar_contato()
        elif escolha == 4:
            excluir_contato()
        elif escolha == 5:
            mostrar_contatos()
        elif escolha == 6:
            sair_programa()

menu()
fluxo_logistico()
reapresentar_menu()