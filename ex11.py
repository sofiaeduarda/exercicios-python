import time

pb = 0
ds = 0

while ds < 5:
    status = input("A peça está boa? (s/n): ")

    if status.lower() == 's':
        pb += 1
        ds = 0
    else:
        ds += 1

print(f"Total de peças boas no lote: {pb}")
time.sleep(1)
print("5 peças defeituosas encontradas seguidas. Encerrando programa.")