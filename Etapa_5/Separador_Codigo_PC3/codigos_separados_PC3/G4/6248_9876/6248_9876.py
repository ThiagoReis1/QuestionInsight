var1 = input("insira 'p' para python, 'c' para 'C' ou 'A' para ambas: ").upper()

cont = 0 

while var1 != 'X':
	if var1 == 'A':
		cont += 1
	var1 = input("insira as letras: ").upper()

print(cont)