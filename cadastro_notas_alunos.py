quantidade_alunos = int(input("Digite o número da quantidade de alunos que serão cadastrados: "))

if quantidade_alunos < 10:
    print("É necessário cadastrar no mínimo 10 alunos! Tente novamente mais tarde.")
    break
    
else:
    alunos = []

    for m in range(quantidade_alunos):
        nome = input("Digite o nome do aluno: ")

        notas = []

        for l in range(3):

            while True:
                nota = float(input("Digite a nota do aluno (0 a 10): "))

                if nota < 0 or nota > 10:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
                    continue

                break

            notas.append(nota)

        media = (notas[0] + notas[1] + notas[2]) / 3

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

    print("\nQuantidade total de alunos cadastrados:", len(alunos))

    for aluno in alunos:
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        nota3 = aluno[3]
        media = aluno[4]
        situacao = aluno[5]

        print("\nAluno:", nome)
        print("Notas:", nota1, nota2, nota3)
        print("Média:", media)
        print("Situação:", situacao)

