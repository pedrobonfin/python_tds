nome = input("Digite seu nome: ")
for i in range(3):
    senha = int(input("Digite sua Senha: "))
    if senha == 123456:
        print(f"Olá {nome}, Bem vindo ao Banco")
        break
    else:
        if i == 2:
            print("Número máximo de tentativas atingido. Vá até o caixa mais próximo.")
        else:
            print(f"Senha incorreta. Você tem apenas mais {3-i-1} tentativas.")

print(f"Olá, {nome}! Seja bem-vindo ao nosso banco!.")
saldo = 0.0

adicionar = float(input("Digite o valor a ser adicionado na sua conta: R$ "))
saldo += adicionar
print(f"Seu saldo atual é de R$ {saldo:.2f}")
