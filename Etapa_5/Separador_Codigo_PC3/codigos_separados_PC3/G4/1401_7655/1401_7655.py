drag= input("Insira o tipo de ataque: ")
qtd= int(input("Quantidade de baforadas: "))

if(drag== "maritimo"):
	nome= "Viserion"
	print(nome)
else:
	nome= "Drogon"
	print(nome) 
	
if (nome== "Viserion"):
	mortes= qtd*40
	print(mortes)
else:
	mortes= qtd*150
	print(mortes) 

	
	
