import time

horas = 0

while horas <= 500:
    print(f"Máquina operando a... {horas} horas")
    time.sleep(1)
    horas += 50

    if horas >= 500:
        print("Alerta! 500 horas atingida.")
        break