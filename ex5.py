horario = int(input("Horário atual (apenas hora): "))

if horario >= 6 and horario <= 12:
    print("Turno da manhã.")
elif horario > 12 and horario <= 18:
    print("Turno da tarde.")
else:
    print("Turno da noite.")