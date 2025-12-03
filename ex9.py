total_consumo = 0

for i in range(1, 6):
    consumo = float(input(f"Digite o consumo da máquina {i} (kWh): "))
    total_consumo += consumo
    
print(f"Consumo total da fábrica: {total_consumo} kWh")