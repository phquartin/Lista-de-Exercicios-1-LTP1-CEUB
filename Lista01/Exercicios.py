
def Ex01():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("Par!")
    else:
        print("Ímpar!")


def Ex02():
    turma = ('André', 'Fernanda', 'Luiz')
    pergunta = input("Digite o nome do aluno: ").capitalize()
    if pergunta in turma:
        print("O aluno está na turma!")
    else:
        print("O aluno não está na turma!")


def Ex03():
    fibonacci = []
    aux = 1
    qtd = int(input("Quantos termos de Fibonacci você quer saber: "))
    for num in range(1, qtd + 1):
        if num == 0 or num == 1:
            fibonacci.append(num)
        else:
            fibonacci.append(aux)
            aux += fibonacci[num - 2]
    print('-' * 40)
    for i in range(len(fibonacci)):
        print(f'Termo {i + 1}: {fibonacci[i]}')
    print('-' * 40)


def Ex04():
    notas = [6.3, 7.5, 9.2, 5.1, 6.8]
    medianotas = sum(notas) / len(notas)
    print(f'Média: {medianotas:.1f}')
    for nota in notas:
        if nota > medianotas:
            print(f'Nota: {nota} Acima da média!')


def Ex05():
    from random import randint
    ganhou = 0
    perdeu = 0
    empate = 0
    while True:
        pc = randint(1, 3)
        print("1 - Papel\n2 - Tesoura\n3 - Pedra\n0 - SAIR")
        user = int(input("Sua escolha: "))
        if user == pc:
            print("\033[1;30mEmpate!\033[m")
            empate += 1
        elif user == 1 and pc == 2 or pc == 3 and user == 2 or user == 3 and pc == 1:
            print("\033[1;31mVocê perdeu!\033[m")
            perdeu += 1
        elif user == 1 and pc == 3 or user == 2 and pc == 1 or user == 3 and pc == 2:
            print("\033[1;32mVocê ganhou!\033[m")
            ganhou += 1
        elif user == 0:
            break
        else:
            print("\033[7;31mERRO!\033[m")
    print(f'Ganhou: {ganhou}\nPerdeu: {perdeu}\nEmpate: {empate}')


def Ex06():
    biblioteca = {'Café Com Deus Pai': ['Junior Rostriola', 2024],
                  'É Assim Que Acaba': ['Collen Hoover', 2016],
                  'Dom Quixote': ['Miguel De Cervantes', 1612],
                  'Um Conto De Duas Cidades': ['Charles Dickens', 1859],
                  'O Senhor Dos Anéis': ['J. R. R. Tolkien', 1954],
                  'O Pequeno Príncipe': ['Antonie De Saint-Exupéry', 1943],
                  'Trono De Vidro': ['Sarah J. Maas', 2018],
                  }
    while True:
        print('\n1 - Listar todos os Livros\t|\t2 - Adicionar um Livro\t\t|\t\t3 - Buscar um livro\n0 - SAIR')
        comando = int(input("Digite o comando: "))
        if comando == 1:
            for chave in biblioteca:
                print('-' * 40)
                print(f'Livro: {chave}\t|\tAutor: {biblioteca[chave][0]}\t|\tAno: {biblioteca[chave][1]}')
        elif comando == 2:
            livroadc = input("Digite o nome do Livro que será adicionado: ").title()
            if livroadc in biblioteca:
                print("\n\033[1;31mERRO!\nLivro já está na lista!\033[m")
                continue
            autor = input("Digite o nome do autor: ").title()
            ano = int(input("Digite o ano: "))
            newlist = list([autor, ano])
            biblioteca.update({livroadc: newlist})
        elif comando == 3:
            tituloBusca = input("Digite o nome do livro: ").title()
            if tituloBusca in biblioteca:
                print('-' * 40)
                print(f'Livro: {tituloBusca}\t|\tAutor: {biblioteca[tituloBusca][0]}\t|\tAno: {biblioteca[tituloBusca][1]}')
                print('-' * 40)
            else:
                print("\033[1;31mERRO!\nLivro não localizado\033[m")
        elif comando == 0:
            break
        else:
            print("\033[1;31mDigite um comando válido!\033[m")
