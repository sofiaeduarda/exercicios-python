import random

vs = random.randint(0, 150)
print(f"Valor do sensor: {vs}") 

if 1 <= vs <= 100:
    print("Sensor OK")
else:
    print("Sensor com problema!")