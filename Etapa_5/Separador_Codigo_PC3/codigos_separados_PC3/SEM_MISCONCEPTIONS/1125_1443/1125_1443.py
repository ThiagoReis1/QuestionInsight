#Igor Rodrigues Chicolet da SIlva
#Universidade Federal do Amazonas - UFAM
#Num de matricula: 21204615 - 13/07/2016

lobo = input("Qual o lobo: ")

if(lobo == "Lady"):
	Stark = "Sansa"
elif(lobo == "Vento Cinzento"):
	Stark = "Robb"
elif(lobo == "Cao Felpudo"):
	Stark = "Rickon"
elif(lobo == "Fantasma"):
	Stark = "Jon Snow"
elif(lobo == "Verao"):
	Stark = "Bran"
elif(lobo == "Nymeria"):
	Stark = "Arya"
else:
	Stark = -1

if(Stark == -1):
	print("Entrada", lobo, "invalida")
else:
	print(Stark)