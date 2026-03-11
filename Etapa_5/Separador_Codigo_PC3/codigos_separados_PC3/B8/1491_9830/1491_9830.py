peso = float(input("digite: "))

if 0 < peso < 5000:
	valor = peso * 0.03 + 20
elif peso < 6000:
	valor = peso * 0.04 + 25
elif peso < 7000:
	valor = peso * 0.05 + 30
elif peso > 7000:
	valor = peso * 0.06 + 35

print(round(valor, 2))