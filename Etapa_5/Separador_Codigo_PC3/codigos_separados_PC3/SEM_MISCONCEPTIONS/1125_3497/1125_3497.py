lobo = input("digite o nome do lobo:")

if(lobo=="Lady"):
	mensagem="Sansa"
	
elif(lobo=="Vento Cinzento"):
	mensagem="Robb"
	
elif(lobo=="Cão Felpudo"):
	mensagem="Rickon"

elif(lobo=="Fantasma"):
	mensagem="Jon Snow"
	
elif(lobo=="Verao"):
	mensagem="Bran"
	
elif(lobo=="Nymeria"):
	mensagem="Arya"
	
else:
	mensagem="Entrada " + lobo + " invalida"
	
print(mensagem)