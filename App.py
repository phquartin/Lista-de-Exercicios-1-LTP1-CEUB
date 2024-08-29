import Lista01.Exercicios as lista01
while True:
    ex = int(input("Digite o número do exercício: "))
    if ex == 1:
        lista01.Ex01()
    elif ex == 2:
        lista01.Ex02()
    elif ex == 3:
        lista01.Ex03()
    elif ex == 4:
        lista01.Ex04()
    elif ex == 5:
        lista01.Ex05()
    elif ex == 6:
        lista01.Ex06()
    else:
        print("Exercício Inválido!")
        continue
    choice = input("Para sair digite 'N' |\tou\t| Digite 'S' para outro exercício").title()
    if 'N' in choice:
        break
