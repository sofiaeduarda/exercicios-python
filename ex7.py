pr = float(input("Digite a produção real: "))
pe = float(input("Digite a produção esperada: "))

ef = (pr / pe) * 100

print(f"Eficiência: {ef:.2f}%")

if ef >= 90:
    print("Classificação: Excelente")
elif ef >= 70: 
    print("Classificação: Boa")
else:
    print("Classificação: Precisa melhorar")