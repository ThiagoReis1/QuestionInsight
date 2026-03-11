var = int(input("Digite o tempo de voo (min): "))

if(var <= 200):
	aux = 5000.00 + (100.00 * var);
else:
	excedente = var - 200;
	aux = 8000.00 + (100 * 200) + (90 * excedente);

print(round(aux,2))

