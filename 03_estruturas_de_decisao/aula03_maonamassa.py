# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
match opcao: 
    case 1:
        print ("Consultar livro")
    case 2:
        print ("Realizar emprestimo")
    case 3:
        print ("Devolver livro")
    case _: 
        print ("Não encontrado") 