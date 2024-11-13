# Sementinha.py

# Listas para armazenar dados
organizacoes = []
campanhas = []
doacoes = []
 
# Função para cadastrar organização
def cadastrar_organizacao(nome, descricao):
    organizacoes.append({"nome": nome, "descricao": descricao})
    print(f'Organização "{nome}" criada com sucesso.')
    return organizacoes
 
# Função para cadastrar campanha
def cadastrar_campanha(nome, organizacao, objetivo, descricao, valor_meta):
    if organizacao not in [organizacao["nome"] for organizacao in organizacoes]:
        print(f'Organização "{organizacao}" nao encontrada. Tente novamente.')
        return
    campanhas.append({
        "nome": nome,
        "organizacao": organizacao,
        "objetivo": objetivo,
        "descricao": descricao,
        "valor_meta": valor_meta,
        "total_doacoes": 0.0,
        "doacoes": []
    })
    print(f'Campanha "{nome}" criada com sucesso para a organização "{organizacao}".')
    return campanhas
 
# Função para listar campanhas
def listar_campanhas():
    if campanhas:
        print('\nCampanhas cadastradas:')
        for index, campanha in enumerate(campanhas, start=1):
            print(f'{index}. {campanha["nome"]} - Organização: {campanha["organizacao"]} - Objetivo: {campanha["objetivo"]} - Meta: R${campanha["valor_meta"]:.2f}')
            if verificar_meta_atingida(campanha["nome"]):
                print(f'   Meta atingida para a campanha "{campanha["nome"]}".')
    else:
        print('\nNenhuma campanha cadastrada.')
 
# Função para realizar doação
def realizar_doacao(email, nome_campanha, valor):
    for campanha in campanhas:
        if campanha["nome"].lower() == nome_campanha.lower():
            if valor <= 0:
                print("Valor de doação inválido. Tente novamente.")
                return
            if not verificar_entrada_email(email):
                return
            doacao = {"email": email, "valor": valor}
            campanha["doacoes"].append(doacao)
            campanha["total_doacoes"] += valor
            print(f'Doação de R${valor:.2f} realizada com sucesso para a campanha "{nome_campanha}".')
            return
    print(f"Campanha '{nome_campanha}' não encontrada.")
 
# Função para verificar se a meta de uma campanha foi atingida
def verificar_meta_atingida(nome_campanha):
    for campanha in campanhas:
        if campanha["nome"].lower() == nome_campanha.lower():
            return campanha["total_doacoes"] >= campanha["valor_meta"]
    return False
 
# Função para validar entradas
def verificar_entrada_email(email):
    if "@" in email and "." in email:
        return True
    print("Email inválido.")
    return False
 
# Função de menu principal
def menuSementinha():
    while True:
        print("\n--- Menu Principal ---")
        print("Bem-vindo ao Sistema de Campanhas do Sementinha!")
        print("1. Cadastrar Organização")
        print("2. Cadastrar Campanha")
        print("3. Listar Campanhas")
        print("4. Realizar Doação")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            nome = input("Digite o nome da Organização: ")
            descricao = input("Digite a descrição da Organização: ")
            cadastrar_organizacao(nome, descricao)
 
        elif opcao == "2":
            nome = input("Digite o nome da Campanha: ")
            organizacao = input("Digite o nome da Organização: ")
            objetivo = input("Digite o objetivo da Campanha: ")
            descricao = input("Digite a descrição da Campanha: ")
            try:
                valor_meta = float(input("Digite o valor da meta da Campanha: "))
                cadastrar_campanha(nome, organizacao, objetivo, descricao, valor_meta)
            except ValueError:
                print("Valor de meta inválido. Digite um número válido.")
 
        elif opcao == "3":
            listar_campanhas()
 
        elif opcao == "4":
            email = input("Digite o email do usuário: ")
            if not verificar_entrada_email(email):
                continue
            nome_campanha = input("Digite o nome da Campanha: ")
            try:
                valor = float(input("Digite o valor da doação: "))
                realizar_doacao(email, nome_campanha, valor)
            except ValueError:
                print("Valor de doação inválido. Digite um número válido.")
 
        elif opcao == "5":
            print("Obrigado por utilizar o Sistema de Campanhas do Sementinha!")
            break
 
        else:
            print("Opção inválida. Tente novamente.")
 
# Iniciar o menu principal
menuSementinha()
 