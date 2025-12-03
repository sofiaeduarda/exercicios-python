produto = input("Digite o tipo de produto (A, B ou C): ").upper()

if produto == "A":
    velocidade = 1
elif produto == "B":
    velocidade = 2
elif produto == "C":
    velocidade = 3
else:
    velocidade = 0
    print("Produto inválido.")