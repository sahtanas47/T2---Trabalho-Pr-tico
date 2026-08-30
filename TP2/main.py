from biblioteca import Biblioteca
from usuario import Usuario
from item import Item
from emprestimo import Emprestimo
from livro import Livro
from hq import HQ
from prateleira import Prateleira
from termcolor import colored, cprint

minha_biblioteca = Biblioteca("Biblioteca IFMG")
prateleira_a = minha_biblioteca.criar_prateleira("A1")
prateleira_b = minha_biblioteca.criar_prateleira("B1")
livro_a = Livro("Dom Casmurro", 1899, 256, "Machado de Assis")
hq_a = HQ("Batman: A Piada Mortal", 1988, 1, "Desconhecido")
livro_b = Livro("Dom Quixote", 1605, 863, "Miguel de Cervantes")
hq_b = HQ("Ultimate Wolverine", 2026, 2, "Desconhecido")

prateleira_a.adicionar_item(livro_a)
prateleira_a.adicionar_item(hq_b)
prateleira_b.adicionar_item(livro_b)
prateleira_b.adicionar_item(hq_a)

usuarios = []
emprestimos = []
usuario_a = Usuario("Sarah Sodre", 13307688509)
usuario_b = Usuario("Beatriz Martins Cangue", "04019635609")
usuarios.append(usuario_a)
usuarios.append(usuario_b)


while True:
    print(colored("\n---🕸️ MENU DA BIBLIOTECA ---", "white" ))
    print(colored("1. Cadastrar Livro", "blue"))
    print(colored("2. Cadastrar Hq", "red"))
    print(colored("3. Cadastrar Usuário", "blue"))
    print(colored("4. Realizar Empréstimo", "red"))
    print(colored("5. Listar Itens na Prateleira", "blue"))
    print(colored("6. Listar Empréstimos", "red"))
    print(colored("7. Devolver empréstimo", "blue"))
    print(colored("8. Listar Usuários", "red"))
    print(colored("0. Sair", "yellow"))

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        titulo = input("Título do livro: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        num_paginas = int(input("Páginas: "))
        Livro = Livro(titulo, ano, num_paginas, autor)
        prateleira_a.adicionar_item(Livro)
        print(colored("🕷 Livro adicionado com sucesso!", "red"))

    elif opcao == "2":
        titulo = input("Título da HQ: ")
        ano = int(input("Ano: "))
        edicao = int(input("Edição nº: "))
        autor = input("Autor: ")
        HQ = HQ(titulo, ano, edicao, autor)
        prateleira_a.adicionar_item(HQ)
        print(colored("🕷 HQ adicionada com sucesso!", "blue"))

    elif opcao == "3":
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF:")
        usuario = Usuario(nome, cpf)
        usuarios.append(usuario)
        print(colored("🕸Usuário cadastrado com sucesso!", "red"))

    elif opcao == "4":
        if not usuarios or not prateleira_a.itens:
            print(colored("🕸️ྀིERRO! É preciso ter pelo menos 1 usuário e 1 item cadastrado!", "light_red", "on_white"))
        else:
            print(colored("Usuários disponíveis:", "green", "on_white"))
            for pos, u in enumerate(usuarios):
                print(f"{pos} - {u.nome}") 

            pos_u = int(input("Digite o número do usuário:"))
            escolha_a = input("Escolha a prateleira que voce deseja encontrar: ")

            if escolha_a == "B1":
                print(colored("Itens disponíveis na prateleira B1: ", "blue", "on_white"))
                for pos, item in enumerate(prateleira_b.itens):
                    print(colored(f"{pos} - {item.titulo}","red"))

                pos_i = int(input("Digite o número do item: "))
                emp = Emprestimo(usuarios[pos_u], prateleira_b.itens[pos_i])

                if emp.realizar_emprestimo():
                    emprestimos.append(emp)
                    print(colored("🕷Empréstimo realizado com sucesso!", "red"))
                    continue
                else:
                    print(colored("🕸Este item já está emprestado!", "yellow", "on_white"))

            elif escolha_a == "A1":
             print(colored("Itens disponíveis na prateleira A1:", "blue", "on_white"))
            for pos, item in enumerate(prateleira_a.itens):
                print(f"{pos} - {item.titulo}")
            pos_i = int(input("Digite o número do item: "))
            emp = Emprestimo(usuarios[pos_u], prateleira_a.itens[pos_i])
            if emp.realizar_emprestimo():
                emprestimos.append(emp)
                print(colored("🕷Empréstimo realizado com sucesso!,", "red"))
            else:
                print(colored("🕸Este item já está emprestado!", "yellow", "on_white"))

    elif opcao == "5":
            escolha = input("Escolha a prateleira desejada:")
            if escolha == ("B1"):
                 print(colored("🕸️ྀི Itens na Prateleira B1:", "blue", "on_white"))
                 prateleira_b.listar_itens()
            else:
             print(colored("\n🕸️ྀི Itens na Prateleira A1:", "red", "on_white"))
             prateleira_a.listar_itens()
    
    elif opcao == "6":
        if not emprestimos:
            print(colored("🕸️๋࣭ ⭑Não há nenhum empréstimo aqui!", "blue"))
        else:
            print(colored("\n🕸Lista de Empréstimos:", "red", "on_white"))
            for emp in emprestimos:
                print(emp.resumir())

    elif opcao == "7":
         if not emprestimos:
              print(colored("🕷 Não há nenhum empréstimo realizado!", "blue"))
         else:
              for posi, emp in enumerate(emprestimos):
                   print(f"{posi} - {emp.usuario.nome} está com {emp.item.titulo}")
              dev = int(input("Digite o número do empréstimo a ser devolvido: "))

              emprestimo_selecionado = emprestimos[dev]
              emprestimo_selecionado.finalizar_emprestimo()
              emprestimos.pop(dev)

    elif opcao == "8":
        if not usuarios:
            print(colored("Nenhum usuário cadastrado.", "red", "on_white"))
        else:
            for usuario in usuarios:
                print(f"O usuário {usuario.nome} de CPF {usuario.cpf} está cadastrado!")
                print(colored("---------------------", "cyan"))       
         
    
    elif opcao == "0":
        print(colored("Saindo do programa...", "yellow"))
        break
    else:
        print(colored("ERRO! Opção inválida. Tente novamente.", "light_red", "on_white"))
         

