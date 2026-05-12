usuarios = []

def cadastrar_usuario():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)

    print("\nUsuário cadastrado com sucesso!\n")


def listar_usuarios():
    if len(usuarios) == 0:
        print("\nNenhum usuário cadastrado.\n")
        return

    print("\n=== USUÁRIOS CADASTRADOS ===")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"""
Usuário {i}
Nome: {usuario['nome']}
Idade: {usuario['idade']}
Email: {usuario['email']}
""")


while True:
    print("=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        print("\nEncerrando sistema...")
        break

    else:
        print("\nOpção inválida!\n")
