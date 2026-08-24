from biblioteca import Biblioteca
from usuario import Usuario
from item import Item
from emprestimo import Emprestimo
from livro import Livro
from hq import HQ

minha_biblioteca = Biblioteca("Biblioteca IFMG")
prateleira_a = minha_biblioteca.criar_prateleira("A1")

usuarios = []
emprestimos = []

while True:
    print("\n--- MENU DA BIBLIOTECA ---")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Hq")
    print("3. Cadastrar Usuário")
    print("4. Realizar Empréstimo")
    print("5. Listar Itens na Prateleira")
    print("6. Listar Empréstimos")
    print("7. Devolver empréstimo")
    print("8. Listar Usuários")
    print("0. Sair")

    opcao = input("Escolha uma opção:")
    if opcao == "1":
        titulo = input("Título do livro: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        num_paginas = int(input("Páginas: "))
        Livro = Livro(titulo, ano, autor, num_paginas)
        prateleira_a.adicionar_item(Livro)
        print("Livro adicionado com sucesso!")

    elif opcao == "2":
        titulo = input("Título da HQ: ")
        ano = int(input("Ano: "))
        edicao = int(input("Edição nº: "))
        HQ = HQ(titulo, ano, edicao)
        prateleira_a.adicionar_item(HQ)
        print("Revista adicionada com sucesso!")

    elif opcao == "3":
        nome = input("Digite seu nome:")
        cpf = input("Digite seu CPF:")
        usuario = Usuario(nome, cpf)
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "4":
        if not usuarios or not prateleira_a.itens:
            print("É preciso ter pelo menos 1 usuário e 1 item cadastrado!")
        else:
            print("\nUsuários disponíveis:")
            for pos, u in enumerate(usuarios):
                print(f"{pos} - {u.nome}")
                
            pos_u = int(input("Digite o número do usuário"))
            print("\nItens disponíveis na prateleira:")
            for pos, item in enumerate(prateleira_a.itens):
                print(f"{pos} - {item.titulo}")
            pos_i = int(input("Digite o número do item: "))

            emp = Emprestimo(usuarios[pos_u], prateleira_a.itens[pos_i])
            
            if emp.realizar_emprestimo():
                emprestimos.append(emp)
                print("Empréstimo realizado com sucesso!")
            else:
                print("Este item já está emprestado!")

    elif opcao == "5":
            print("\nItens na Prateleira A1:")
            prateleira_a.listar_itens()
    
    elif opcao == "6":
            print("\nLista de Empréstimos:")
            for emp in emprestimos:
                print(emp.resumir())

    elif opcao == "7":
         if not emprestimos:
              print("Não há nenhum empréstimo realizado!")
         else:
              for posi, emp in enumerate(emprestimos):
                   print(f"{posi} - {emp.usuario.nome} está com {emp.item.titulo}")
              dev = int(input("Digite o número do empréstimo a ser devolvido"))
              emprestimo_selecionado = emprestimos[dev]
              emprestimo_selecionado.finalizar_emprestimo()
              emprestimos.pop(dev)
    elif opcao == "8":
        for Usuario in usuarios:
            print(f"Nome: {Usuario.nome}")
            print(f"Cpf: {Usuario.cpf}")
            print("---------------------")               
         
    
    elif opcao == "0":
            print("Saindo do programa...")
            break
    
    else:
            print("Opção inválida! Tente novamente.")
