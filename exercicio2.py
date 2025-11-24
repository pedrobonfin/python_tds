horas = int(input("Quantas horas você assiste por semana a Netflix: "))
ass = float(input("Valor mensal da assinatura: "))

print(f"Por hora, você gasta: R${ass/(horas*4):.02f}")