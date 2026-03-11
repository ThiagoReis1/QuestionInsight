linguagem = input("Digite a linguagem utilizado: ").upper()
cont = 0

while linguagem != "X":
	if linguagem == "A":
		cont = cont + 1
	linguagem = input("Digite a linguagem utilizada: ").upper()
	
print(cont)