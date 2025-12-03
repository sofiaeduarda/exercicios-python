import time

estoque = int(input("Digite a quantidade atual no estoque: "))

if estoque < 50:
    print(f"Estoque baixo! Apenas {estoque} unidades.")
    time.sleep(1)
    print("Fazer reposição recomendado.")
else:
    print(f"Estoque normal! {estoque} unidades.")