q_numero = int(input("Digite um valor:"))

cont = 0

while q_numero != -1:
	if (q_numero >= 45) and (q_numero <= 150):
		cont = cont + 1
	q_numero = int(input("Digite um valor:"))
print(cont)