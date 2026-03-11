tipo = input()
comida = int(input())
acai = int(input())

total = acai * 12.0

if tipo == 'T':
	total += comida * 4.5
else:
	total += comida * 5.0

print(total)