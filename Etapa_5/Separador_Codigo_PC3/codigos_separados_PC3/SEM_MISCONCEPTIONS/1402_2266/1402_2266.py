nome = input("Qual o nome da arma?")
fator = int(input("Qual o fator de sucesso?"))

if nome == "machado":
	dano = 30*fator/10
else:
	dano = 5 + 20*fator/10
	
print(dano)
