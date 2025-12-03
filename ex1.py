temp = float(input("Insira a temperatura atual em °C: "))

if temp > 80:
    print("Alerta! Estado Crítico.")
elif temp > 60:
    print("Aviso! Temperatura elevada.")
else:
    print("Temperatura normal.")