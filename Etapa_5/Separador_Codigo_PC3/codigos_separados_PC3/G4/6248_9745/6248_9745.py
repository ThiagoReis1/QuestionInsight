ent = input("linguagem:").upper()

cont = 0

while ent != 'X':
	if ent == 'A':
		cont = cont + 1
	ent = input("linguagem:").upper()
print(cont)