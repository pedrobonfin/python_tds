preco_camisa = 12.5
quant_camisa = int(input("Quantas camisas você deseja comprar: "))
valor = 12.5 * quant_camisa

if quant_camisa <= 5 and quant_camisa > 0:
    valor_descontado = valor - (valor*0.03)
    print(f"Seu desconto é de 3% na sua compra de R${valor}, o valor final da compra é de RS{valor_descontado}")

if quant_camisa > 5 and quant_camisa <= 10:
    valor_descontado = valor - (valor*0.05)
    print(f"Seu desconto é de 5% na sua compra de R${valor}, o valor final da compra é de RS{valor_descontado}")

if quant_camisa > 10:
    valor_descontado = valor - (valor*0.07)
    print(f"Seu desconto é de 7% na sua compra de R${valor}, o valor final da compra é de RS{valor_descontado}")