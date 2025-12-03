total_producao = 0

for hora in range(1, 9):
    producao = int(input(f"Digite a produção da {hora}ª hora: "))
    total_producao += producao

print(f"Total produzido no turno: {total_producao} unidades.")