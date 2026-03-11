nome=input("nome da arma : ")
fator=int(input("entre com o fator"))

if (nome=="machado"):
	dano=30*fator/10
else:
	dano=5+20*fator/10
	
print(int(dano))
