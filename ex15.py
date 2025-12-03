tp = 0
mp = 0
lm = 0

for i in range(1, 6):
    producao = int(input(f"Digite a produção da linha {i}: "))
    tp += producao

    if producao > mp:
        mp = producao
        lm = i

print(f"Produção total: {tp}")
print(f"Linha com maior produção: Linha {lm} ({mp} unidades)")