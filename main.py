import os
clear = lambda: os.system('clear')
clear()

opcao = 1
while(opcao != 0):
    
    print("Atividade de PARADIGMAS")
    print(" 1 - QUESTÃO 01")
    print(" 2 - QUESTÃO 02")
    print(" 3 - QUESTÃO 03")
    print(" 4 - QUESTÃO 04")
    print(" 5 - QUESTÃO 05")
    print(" 0 - PARA SAIR")
    print("")
    opcao = int(input("Digite o desejado: "))
    clear()

    if(opcao == 1):
        print("PESSOA MAIS VELHA")
        print("Digite o nome da primeira pessoa: ")
        p1 = input("Nome: ")
        i1 = int(input("Idade: "))
        print("Digite o nome da Segunda pessoa: ")
        p2 = input("Nome: ")
        i2 = int(input("Idade: "))

        if(i1 > i2):
            print("pessoa mais velha: {}".format(p1))
        else:
            print("pessoa mais velha: {}".format(p2))

        print("")
        
    elif(opcao == 2):
        print("MEDIA DE SALÁRIO")
        print("Digite o nome do primeiro funcionairo: ")
        p1 = input("Nome: ")
        s1 = float(input("Salário: "))
        print("Digite o nome do Segundo funcionairo: ")
        p2 = input("Nome: ")
        s2 = float(input("Salário: "))

        media =(s1 + s2 ) / 2

        print("Salário médio =  {}".format(media))

        print("")

    elif(opcao == 3):
        from retangulo import Retangulo

        print("LARGURA E ALTURA DE UM RETÂNGULO")
        print("Entre com a largura e altura do retângulo: ")
        L1 = float(input("Largura: "))
        A1 = float(input("Altura: "))

        retangulo = Retangulo(A1,L1)

        area = retangulo.Area(A1,L1)
        perimetro = retangulo.Perimetro(A1, L1)
        diagonal = retangulo.Diagonal(A1, L1)

        print("Area: {}".format(area))
        print("Perímetro: {}".format(perimetro))
        print("Diagonal: {}".format(diagonal))

        print("")

    elif(opcao == 4):
        from funcionario import Funcionario
        print("ATUALIZAÇÃO DE DADOS")

        print("Digite um funcionario")
        nome = input("Nome: ")
        salario = float(input("Salario: "))
        imposto = float(input("Imposto: "))
        funcionario1 = Funcionario(nome, salario, imposto)
        liquido = funcionario1.SalarioLiquido(salario, imposto)
        print(" ")
        print("Funcionairo : {} , R$ {}".format(nome, liquido))
        comis = float(input("Digite a porcentagem para aumentar o salário: "))
        aument = funcionario1.AumentoSalario(salario, liquido, comis)

        print("Dados Atualizados : {} R$ {}".format(nome, aument))

        print("")

    elif(opcao == 5):

        print("APROVADO OU REPROVADO")
        nome = input("Nome do Aluno: ")
        nota1 = float(input("Primeira nota : "))
        nota2 = float(input("Segunda nota : "))
        nota3 = float(input("Terceira nota : "))

        notas = (nota1 + nota2 + nota3)
        print("")
        vb = 60.0
        vr = vb - notas
        if(notas >= vb):
            print("Nota final = {:.2f}".format(notas))
            print("Aprovado")
        else:
            print("Nota final = {:.2f}".format(notas))
            print("Reprovado")
            print("Faltaram {:.2f} pontos".format(vr))
        print("")

    elif(opcao == 0):
        break
    else:
        print("Valor informado inválido! ")