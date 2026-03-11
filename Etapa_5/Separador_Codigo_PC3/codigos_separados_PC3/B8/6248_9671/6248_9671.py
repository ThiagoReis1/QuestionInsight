linguagem = input("insira o que voce programa (C/P/A/X): ").upper()

cont = 0

while linguagem != 'X':
	if linguagem == 'P' or linguagem == 'C':
		cont = cont + 0
		linguagem = input("insira o que voce programa (C/P/A/X): ").upper()
		
	elif linguagem == 'A':
		cont = cont + 1
		linguagem = input("insira o que voce programa (C/P/A/X): ").upper()
	
print(cont)

