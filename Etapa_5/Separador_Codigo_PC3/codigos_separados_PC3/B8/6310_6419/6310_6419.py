from numpy import*
i = 0
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0

s = input("Produtos: ").upper()

while i < len(s):
	if s[i] == "M":
		cont = cont + 7.25
		cont1 = cont1 + 1
	elif s[i] == "P":
		cont = cont + 4.75
		cont2 = cont2 + 1
	elif s[i] == "R":
		cont = cont + 3.50
		cont3 = cont3 + 1
	i = i + 1

t = round(cont, 2)
print(t,cont1,cont2,cont3)
		
	
	
	
	
