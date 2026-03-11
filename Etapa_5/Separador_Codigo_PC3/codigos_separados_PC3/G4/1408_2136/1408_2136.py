a = input("katana ou sabre? ")
d =float(input("destreza do personagem: "))
d_1 =int(input("numero sorteado no dado 1: "))
d_2 = int(input("numero sorteado no dado 2: "))
			 
s = d_1 + d_2

if(a == "sabre"):
		dano = s + 2*d	 
	
else:
		dano = 2*s + d
	
print(dano)
			 