c = float(input("Digite o consumo de minutos: "))

if c <= 100: 
	p = 1.20 * c
else: 
	p = 1.40 * c + 25

print(round(p, 2))