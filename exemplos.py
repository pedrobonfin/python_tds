ex1 = list(range(10, 16))  # Incremento = 1: [10, 11, 12, 13, 14, 15]
ex2 = list(range(10, 16, 2))  # Incremento = 2: [10, 12, 14]
ex3 = list(range(16, 10, -1))  # Incremento = -1: [16, 15, 14, 13, 12, 11]
ex4 = list(range(16, 10, -2))  # Incremento = -2: [16, 14, 12]

print(ex1, ex2, ex3, ex4)

print('Operação de Divisão')
while True:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    if n2 == 0:
        print('Divisor não pode ser 0.')
        break
    print(f"{n1} / {n2} = {(n1/n2) :.2f}")
    print('Fim da Operação de Divisão')