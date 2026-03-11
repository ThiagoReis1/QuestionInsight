s = input("Diga a letra ").upper()

i = 0
cont = 0
cont1 = 0
cont2 = 0

var = 0
while (i < len(s)):
	
	if ( s[i] == "B"):
		cont = cont + 1
		var = var + 3.75
	
	elif (s[i] == "C"):
		cont1 =  cont1 + 1
		var = var + 7.90
	
	elif (s[i] == "E"):
		cont2 = cont2 + 1
		var = var + 9.85
	
	i =  i + 1
	
print(round(var, 2))
print(cont, cont1, cont2)