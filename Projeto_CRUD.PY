contatos = {
    "Mariana Alves": "98817-5624",
    "Ana Duarte": "98745-2310",
    "Lucas Henrique": "99632-7481",
    "Gabriel Souza": "99104-8367",
    "Isabela Martins": "98563-1942",
    "Rafael Oliveira": "99721-4508",
    "Camila Ferreira": "98234-6719",
    "Pedro Augusto": "99385-2076",
    "Larissa Costa": "98642-3157",
    "João Victor": "91745-2310",
    "Beatriz Carvalho": "90632-7481",
    "Matheus Rocha": "98819-5624",
    "Sofia Mendes": "99004-8367",
    "Daniel Ribeiro": "90563-1942",
    "Juliana Barros": "99720-4508"
}

def mostrar_opcoes():
    print("Bem-vindo(a) ao Portal de Operações! Veja as opções de execução disponíveis:")
    print("1 - Pesquisar contato")
    print("2 - Adicionar contato")
    print("3 - Excluir contato")
    print("4 - Mostrar todos os contatos")
    print("5 - Editar contato")
    print("6 - Sair do programa")

def obter_opcao():
    while True:
        try:
            escolha = int(input("Selecione a execução desejada de acordo com seu número correspondente: "))
            if escolha in [1, 2, 3, 4, 5, 6]:
                return escolha
            else:
                print("Opção inválida. Por favor, selecione uma das opções indicadas acima.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número correspondente à opção desejada.")

def pesquisar_contato():
    while True:
        busca_tipo = input("Gostaria de procurar por nome ou por número? ").strip()
        if busca_tipo.lower() == "nome" or busca_tipo.lower() == "por nome":
            busca = input("Qual contato deseja encontrar? ").strip()
            if busca in contatos:
                por_nome = contatos[busca]
                print(f"Aqui está: {busca} : {por_nome}.")
                break
            else:
                print("Contato não encontrado.")
        elif (busca_tipo.lower() == "número" or
              busca_tipo.lower() == "numero" or
              busca_tipo.lower() == "por número" or
              busca_tipo.lower() == "por numero"):
            busca_2 = input("Qual número deseja encontrar? ").strip()
            for nome, numero in contatos.items():
                if busca_2 == numero:
                    print(f"Aqui está: {nome} : {numero}.")
                    break
            else:
                print("Contato não encontrado.")
                continue
            break
        else:
            print("Não existe tal opção. Por favor, escolha entre nome ou número.")

def adicionar_contato():
    while True:
        adicao_nome = input("Informe o nome do contato para adicionar: ").strip()
        adicao_numero = input("Informe o número do contato para adicionar: ").strip()
        if not adicao_nome:
            print("O nome não pode ficar vazio.")
            continue
        if not adicao_numero:
            print("O número não pode ficar vazio.")
            continue
        if adicao_nome in contatos:
            print("Já existe um contato com esse nome. Informe o nome do contato para adicionar:")
            continue
        if adicao_numero in contatos.values():
            print("Já existe um contato com esse número. Informe o número do contato para adicionar:")
            continue
        confirmar = input(f"Por favor confirme o contato: {adicao_nome} : {adicao_numero}. Digite 'sim' para confirmar: ")
        if confirmar.lower() == "sim":
            contatos[adicao_nome] = adicao_numero
            print(f"Pronto! O contato {adicao_nome} foi adicionado à lista de contatos.")
            break
        elif confirmar.lower() == "não" or confirmar.lower() == "nao":
            print("Contato não confirmado. As informações serão solicitadas novamente.")
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")

def excluir_contato():
    excluir = input("Qual contato deseja excluir? ").strip()
    if excluir in contatos:
        del contatos[excluir]
        print(f"O contato {excluir} foi excluído com sucesso.")
    else:
        print("Contato não encontrado.")

def mostrar_contatos():
    print("Aqui estão todos os contatos disponíveis:")

    for nome, numero in contatos.items():
        print(f"{nome} : {numero}")

def editar_contato():
    while True:
        editar = input("Qual contato deseja editar? ").strip()
        if editar in contatos:
            nome_editado = input("Informe o novo nome do contato: ").strip()
            numero_editado = input("Informe o novo número do contato: ").strip()
            if not nome_editado:
                print("O nome não pode ficar vazio.")
                continue
            elif not numero_editado:
                print("O número não pode ficar vazio.")
                continue
            elif nome_editado in contatos and nome_editado != editar:
                print("Já existe outro contato com esse nome.")
                continue
            elif numero_editado in contatos.values() and numero_editado != contatos[editar]:
                print("Já existe outro contato com esse número.")
                continue
            elif nome_editado == editar:
                contatos[editar] = numero_editado
                print(f"O número de {editar} foi atualizado para {numero_editado}.")
                break
            else:
                contatos[nome_editado] = numero_editado
                del contatos[editar]
                print(f"O contato {editar} foi editado para {nome_editado} : {numero_editado}.")
        else:
            print("Contato não encontrado.")

def sair_programa():
    print("Obrigado por utilizar o Portal de Operações! Até a próxima.")

while True:
    mostrar_opcoes()
    escolha = obter_opcao()
    if escolha == 1:
        pesquisar_contato()
    elif escolha == 2:
        adicionar_contato()
    elif escolha == 3:
        excluir_contato()
    elif escolha == 4:
        mostrar_contatos()
    elif escolha == 5:
        editar_contato()
    elif escolha == 6:
        sair_programa()
        break