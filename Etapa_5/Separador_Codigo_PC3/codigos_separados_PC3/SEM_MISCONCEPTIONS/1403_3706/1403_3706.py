
nome_armadura= input("")
fator= int(input(""))

if( nome_armadura.lower() == "malha"):
	cota= (15 * fator)- 1
else:
	cota =(20 * fator) - 18
	
print(cota)