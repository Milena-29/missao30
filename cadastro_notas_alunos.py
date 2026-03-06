#Solicitar ao usuário a digitar a quantidade total de alunos
quantidade_alunos = int(input("Digite o número da quantidade de alunos que serão cadastrados: "))

while True:

    # Verfificação se a quantidade de alunos é menos que 10, caso seja, exibe uma mensagem de erro e encerra o programa.
    if quantidade_alunos < 10:
        print("\nÉ necessário cadastrar no mínimo 10 alunos! Tente novamente mais tarde.")
        break

    else:
        print("Quantidade válida de alunos! Prosseguindo com o cadastro...")

    # Criaçãon de uma lista para armanezar os dados dos alunos
    alunos = []

    for m in range(quantidade_alunos):

        # Pedir ao usuário para que digite o nome do aluno
        nome = input("\nDigite o nome do aluno: ")


        # Criação de uma lista para armanezar as notas do aluno
        notas = []

        for l in range(3):

            while True:

             # Solicitar ao usuário para digitar as três notas do aluno  
                nota = float(input("Digite a nota do aluno (0 a 10): "))

                if nota < 0 or nota > 10:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
                    continue

                break

            notas.append(nota)

        # Cálcula da média das notas dos alunos
        media = (notas[0] + notas[1] + notas[2]) / 3

        # Verificação das notas para verificar se o aluno será aprovado,recuperação,reprovado
        if media >= 7:
            situacao = "Aprovado"

        elif media >= 5:
            situacao = "Recuperação"

        else:
            situacao = "Reprovado"

        alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

    print("\nQuantidade total de alunos cadastrados:", len(alunos))

    t = len(alunos)

    for i in range(0, t, 1):

        nome = alunos[i][0]
        nota1 = alunos[i][1]
        nota2 = alunos[i][2]
        nota3 = alunos[i][3]
        media = alunos[i][4]
        situacao = alunos[i][5]

        print("\nAluno:", nome)
        print("Notas:", nota1, nota2, nota3)
        print("Média:", media)
        print("Situação:", situacao, "\n")

    break
