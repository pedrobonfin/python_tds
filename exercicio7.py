print("Exercicio1:\n")

while True:
    num = int(input("Com quantos números você quer fazer a média? "))
    num2 = 0
    if(num < 0):
        print("Número negativo")
        break
    else:
        for i in range(num):
            num1 = int(input("Digite o número: "))
            num2 += num1
            num2/num
            print(f"Média {num2/num}")
            break