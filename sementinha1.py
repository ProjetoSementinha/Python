# Listas globais para armazenar usuários, projetos e campanhas
usuarios = []
projetos = []
campanhas = []


class Usuario:
    def __init__(self, nome, email, cpf, telefone, endereco):
        """Inicia um novo usuario com os dados fornecidos.

        :param str nome: nome do usuario
        :param str email: email do usuario
        :param str cpf: cpf do usuario
        :param str telefone: telefone do usuario
        :param str endereco: endereco do usuario
        :param list doacoes: lista de doacoes realizadas pelo usuario
        """
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.doacoes = []


class Projeto:
    def __init__(self, nome, descricao):
        """Inicia um novo projeto com os dados fornecidos.

        :param str nome: nome do projeto
        :param str descricao: descricao do projeto
        :param list campanhas: lista de campanhas relacionadas ao projeto
        """
        self.nome = nome
        self.descricao = descricao
        self.campanhas = []


class Campanha:
    def __init__(self, nome, projeto, objetivo, descricao, valor_meta):
        """Inicia uma nova campanha com os dados fornecidos.

        :param str nome: nome da campanha
        :param Projeto projeto: projeto relacionado a campanha
        :param str objetivo: objetivo da campanha
        :param str descricao: descricao da campanha
        :param float valor_meta: valor meta da campanha
        :param float total_doacoes: total de doacoes recebidas pela campanha
        :param list doacoes: lista de doacoes recebidas pela campanha
        """
        self.nome = nome
        self.projeto = projeto
        self.objetivo = objetivo
        self.descricao = descricao
        self.valor_meta = valor_meta
        self.total_doacoes = 0.0
        self.doacoes = []

    def atualizar_total_doacoes(self):
        """Atualiza o total de doacoes recebidas pela campanha.

        O total de doacoes e atualizado somando o valor de todas as doacoes
        recebidas pela campanha.
        """
        self.total_doacoes = sum(doacao.valor for doacao in self.doacoes)

    def verificar_meta_atingida(self):
        """Verifica se a campanha ja atingiu a meta.

        A campanha e considerada como tendo atingido a meta se o total de
        doacoes recebidas for maior ou igual a meta definida para a campanha.

        :return bool: True se a campanha ja atingiu a meta, False caso contrario
        """
        return self.total_doacoes >= self.valor_meta


class Doacao:
    def __init__(self, valor, usuario, campanha):
        """Inicia uma nova doacao com os dados fornecidos.

        :param float valor: valor da doacao
        :param Usuario usuario: usuario que realizou a doacao
        :param Campanha campanha: campanha que recebeu a doacao
        """
        self.valor = valor
        self.usuario = usuario
        self.campanha = campanha


# Funções de validação de dados
def validar_cpf(cpf):
    """Verifica se o CPF fornecido e valido.

    Um CPF e considerado valido se tiver 14 caracteres e todos eles forem
    digitos.

    :param str cpf: CPF a ser verificado
    :return bool: True se o CPF for valido, False caso contrario
    """
    if len(cpf) != 14 or not cpf.isdigit():
        return False
    return True


def validar_email(email):
    """
    Verifica se o email fornecido e valido.

    Um email e considerado valido se tiver um "@" e um "." no seu conteudo.

    :param str email: email a ser verificado
    :return bool: True se o email for valido, False caso contrario
    """
    if "@" not in email or "." not in email:
        return False
    return True


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    """
    Cadastra um novo usuario no sistema.

    Solicita o nome, email, CPF, telefone e endereco do usuario e verifica se
    os dados fornecidos sao validos. Se sim, instancia um novo objeto Usuario
    com os dados fornecidos e o adiciona na lista de usuarios.
    """
    nome = input("\nDigite o nome do usuário: ")
    email = input("Digite o email: ")
    if not validar_email(email):
        print("\nEmail inválido. Tente novamente.")
        return
    cpf = input("Digite o CPF: ")
    if not validar_cpf(cpf):
        print("\nCPF inválido. Tente novamente.")
        return
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")

    # Verifica se o CPF ou email ja estao cadastrados
    if any(u.cpf == cpf or u.email == email for u in usuarios):
        print("\nCPF ou email já cadastrado. Tente novamente.")
        return

    usuarios.append(Usuario(nome, email, cpf, telefone, endereco))
    print(f"Usuário {nome} cadastrado com sucesso!")


# Função para cadastrar um novo projeto
def cadastrar_projeto():
    """
    Cadastra um novo projeto no sistema.

    Solicita o nome e descrição do projeto ao usuário e verifica se o nome do
    projeto já está cadastrado. Se não estiver, cria uma nova instância do
    projeto e o adiciona à lista de projetos.
    """
    nome = input("\nDigite o nome do projeto: ")
    descricao = input("Digite a descrição do projeto: ")

    # Verifica se o projeto já está cadastrado pelo nome
    if any(p.nome == nome for p in projetos):
        print("\nProjeto já cadastrado. Tente novamente.")
        return

    # Cria uma nova instância do projeto e adiciona à lista
    projeto = Projeto(nome, descricao)
    projetos.append(projeto)
    print(f"Projeto {nome} cadastrado com sucesso!")


# Função para criar uma campanha
def criar_campanha():
    """
    Cria uma nova campanha associada a um projeto existente.

    Solicita ao usuário a escolha de um projeto existente, além de detalhes
    da campanha como nome, objetivo, descrição e valor da meta. Se os dados
    forem válidos, cria a campanha e a associa ao projeto escolhido.
    """
    if not projetos:
        print("\nNenhum projeto cadastrado. Cadastre um projeto primeiro.")
        return

    # Exibir lista de projetos para o usuário escolher
    print("\nEscolha um projeto para a campanha:")
    for i, projeto in enumerate(projetos, start=1):
        print(f"{i}. {projeto.nome}")
    escolha = int(input("Digite o número do projeto: ")) - 1

    # Verificar se a escolha é válida
    if escolha < 0 or escolha >= len(projetos):
        print("\nEscolha inválida.")
        return
    projeto = projetos[escolha]

    # Solicitar detalhes da campanha
    nome = input("Digite o nome da campanha: ")
    objetivo = input("Digite o objetivo da campanha: ")
    descricao = input("Digite a descrição da campanha: ")

    try:
        # Solicitar e converter o valor da meta
        valor_meta = float(input("Digite o valor da meta da campanha: R$ "))

        # Criar nova campanha e associá-la ao projeto
        campanha = Campanha(nome, projeto, objetivo, descricao, valor_meta)
        campanhas.append(campanha)
        projeto.campanhas.append(campanha)
        print(f"Campanha {nome} criada com sucesso para o projeto {projeto.nome}!")
    except ValueError:
        print("\nValor inválido para a meta da campanha.")


# Função para realizar uma doação
def realizar_doacao():
    """
    Realiza uma doação para uma campanha.

    Solicita o email do usuário que deseja doar, escolhe uma campanha e o valor da doação.
    Cria uma instância de Doacao com os dados fornecidos e atualiza as listas de doações do
    usuário e da campanha.
    """
    if not campanhas:
        print("\nNenhuma campanha cadastrada. Cadastre uma campanha primeiro.")
        return

    # Solicita o email do usuário que deseja doar
    email_usuario = input("\nDigite o email do usuário que deseja doar: ")
    usuario = next((u for u in usuarios if u.email == email_usuario), None)
    if not usuario:
        print("\nUsuário não encontrado.")
        return

    # Exibe as opções de campanhas para o usuário escolher
    print("\nEscolha uma campanha para doar:")
    for i, campanha in enumerate(campanhas, start=1):
        print(f"{i}. {campanha.nome} - Projeto: {campanha.projeto.nome}")
    escolha = int(input("Digite o número da campanha: ")) - 1
    if escolha < 0 or escolha >= len(campanhas):
        print("\nEscolha inválida.")
        return
    campanha = campanhas[escolha]

    # Solicita o valor da doação
    try:
        valor = float(input("Digite o valor da doação: R$ "))
        doacao = Doacao(valor, usuario, campanha)
        usuario.doacoes.append(doacao)
        campanha.doacoes.append(doacao)
        campanha.atualizar_total_doacoes()
        print(
            f"Doação de R${valor:.2f} realizada com sucesso para a campanha {campanha.nome}!"
        )
        if campanha.verificar_meta_atingida():
            print(f"A meta da campanha {campanha.nome} foi atingida!")
        else:
            print(f"A campanha {campanha.nome} ainda não atingiu a meta.")
    except ValueError:
        print("\nValor inválido.")


# Função para listar doações de um usuário por email
def listar_doacoes_por_usuario(email_usuario):
    """
    Lista todas as doações realizadas por um usuário.

    Solicita o email do usuário e lista todas as doações realizadas por ele,
    exibindo o valor da doação e a campanha para a qual foi realizada.
    """
    usuario = next((u for u in usuarios if u.email == email_usuario), None)
    if not usuario:
        print("\nUsuário não encontrado.")
        return
    if not usuario.doacoes:
        print("\nO usuário não fez nenhuma doação.")
        return
    print(f"\nDoações realizadas por {usuario.nome} ({usuario.email}):")
    for doacao in usuario.doacoes:
        # Exibe o valor da doação e a campanha para a qual foi realizada
        print(f" - R${doacao.valor:.2f} para a campanha {doacao.campanha.nome}")


# Função para listar campanhas e seu status
def listar_campanhas():
    """
    Lista todas as campanhas cadastradas e seus detalhes.

    Exibe o nome, projeto associado, objetivo, valor da meta, total arrecadado
    e o status de cada campanha (atingida ou não atingida).
    """
    if not campanhas:
        print("\nNenhuma campanha cadastrada.")
        return

    print("\nCampanhas cadastradas:")
    for campanha in campanhas:
        # Verifica se a meta da campanha foi atingida
        status = "Atingida" if campanha.verificar_meta_atingida() else "Não atingida"
        # Exibe os detalhes da campanha
        print(
            f" - {campanha.nome} (Projeto: {campanha.projeto.nome}) - Objetivo: {campanha.objetivo} "
            f"- Meta: R${campanha.valor_meta:.2f} - Arrecadado: R${campanha.total_doacoes:.2f} - Status: {status}"
        )


# Função para salvar dados formatados
def salvar_dados():
    """
    Salva os dados de usuários, projetos e campanhas em arquivos texto formatados.

    Os arquivos gerados terão o seguinte formato:
        - dados_usuarios.txt: um bloco por usuário, com os dados de nome, email, CPF, telefone, endereço e doações realizadas;
        - dados_projetos.txt: um bloco por projeto, com os dados de nome e descrição;
        - dados_campanhas.txt: um bloco por campanha, com os dados de nome, projeto, objetivo, descrição, valor da meta e total arrecadado.
    """

    with open("dados_usuarios.txt", "w") as f:
        f.write("=== Usuários ===\n")
        for usuario in usuarios:
            # Escreve os dados do usuário
            f.write(
                f"Nome: {usuario.nome}\nEmail: {usuario.email}\nCPF: {usuario.cpf}\nTelefone: {usuario.telefone}\nEndereço: {usuario.endereco}\n"
            )

            # Escreve as doações realizadas pelo usuário
            f.write("Doações:\n")
            for doacao in usuario.doacoes:
                f.write(
                    f"  - R${doacao.valor:.2f} para campanha {doacao.campanha.nome}\n"
                )

            # Adiciona uma linha em branco entre os usuários
            f.write("\n")

    with open("dados_projetos.txt", "w") as f:
        f.write("=== Projetos ===\n")
        for projeto in projetos:
            # Escreve os dados do projeto
            f.write(f"Nome: {projeto.nome}\nDescrição: {projeto.descricao}\n\n")

    with open("dados_campanhas.txt", "w") as f:
        f.write("=== Campanhas ===\n")
        for campanha in campanhas:
            # Escreve os dados da campanha
            f.write(
                f"Nome: {campanha.nome}\nProjeto: {campanha.projeto.nome}\nObjetivo: {campanha.objetivo}\nDescrição: {campanha.descricao}\nMeta: R${campanha.valor_meta}\nTotal Doado: R${campanha.total_doacoes}\n\n"
            )
    print("Dados salvos com sucesso.")


# Função principal de menu
def exibir_menu():
    """
    Exibe o menu principal do sistema, permitindo que o usuário escolha uma das seguintes opções:

        1. Cadastrar Usuário
        2. Cadastrar Projeto
        3. Criar Campanha
        4. Listar Campanhas
        5. Realizar Doação
        6. Listar Doações por Usuário
        7. Salvar Dados
        0. Sair

    O menu é exibido em loop até que o usuário escolha a opção de sair (0).

    :return: None
    """
    while True:
        # Exibe as opções do menu
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Projeto")
        print("3. Criar Campanha")
        print("4. Listar Campanhas")
        print("5. Realizar Doação")
        print("6. Listar Doações por Usuário")
        print("7. Salvar Dados")
        print("0. Sair")

        # Solicita a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Chama a função correspondente à opção escolhida
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cadastrar_projeto()
        elif opcao == "3":
            criar_campanha()
        elif opcao == "4":
            listar_campanhas()
        elif opcao == "5":
            realizar_doacao()
        elif opcao == "6":
            email_usuario = input("\nDigite o email do usuário: ")
            listar_doacoes_por_usuario(email_usuario)
        elif opcao == "7":
            salvar_dados()
        elif opcao == "0":
            print("Encerrando o programa... Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Iniciar o Menu
if __name__ == "__main__":
    exibir_menu()
