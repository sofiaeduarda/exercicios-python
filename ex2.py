prod = int(input("Digite a quantidade produzida: "))

meta = 1000

if prod >= meta:
    print("Meta atingida!")
else:
    faltam = meta - prod
    print(f"Meta não atingida! Faltam {faltam} para atingir.")