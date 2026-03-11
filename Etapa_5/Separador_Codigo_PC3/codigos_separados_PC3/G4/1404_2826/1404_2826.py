ataque=input("Nome: ")
D1=int(input("Sorteio 1: "))
D2=int(input("Sorteio 2: "))
D3=int(input("Sorteio 3: "))
if(ataque=="Aameul"):
	dano = 8+D1+D2+D3
	print(dano)
else:
	dano=2*(D1+D2+D3)
	print(dano)