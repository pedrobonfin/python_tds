dolar = 5.31
euro = 6.16
reais = float(input("Quantos reais você quer converter: "))

print(f"R$ {reais}\nHoje, o USD$ vale R${dolar}, e o Euro vale R${euro}\nVocê tem USD{reais/dolar:.2f} e EUR{reais/euro:.2f}")