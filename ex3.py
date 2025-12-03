peso = float(input("Insira o peso da peça (KG): "))

if peso <= 0.5:
    print("Leve!")
elif peso <= 2:
    print("Média!")
elif peso <= 5:
    print("Pesada!")
else:
    print("Muito pesada!")