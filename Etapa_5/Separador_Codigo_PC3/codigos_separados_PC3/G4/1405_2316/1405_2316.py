ataque = input("ataque: ")
D1 = int(input("D1: "))
D2 = int(input("D2: "))

if(ataque.lower() == "grito"):
	dano = 6+D1+D2
else:
	dano = (D1*D1)+(2*D1*D2)+(D2*D2)
	
print(int(dano))