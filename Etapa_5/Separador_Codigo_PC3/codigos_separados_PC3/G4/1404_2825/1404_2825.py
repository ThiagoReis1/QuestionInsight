nome = input("nome da cabeca:")
D1 = int(input("valor sorteado dado 1:"))
D2 = int(input("valor sorteado dado 2:"))
D3 = int(input("valor sorteado dado 3:"))

#pontuacao

p1 = 8 +(D1+D2+D3)
p2 = 2*(D1+D2+D3)
if(nome == "Aameul"):
	print(p1)
	
else:
	print(p2)