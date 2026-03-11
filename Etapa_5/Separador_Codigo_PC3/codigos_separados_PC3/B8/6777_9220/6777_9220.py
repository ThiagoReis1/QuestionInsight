ano_nasc = int(input("Digite o ano de nascimento: "))
pais = input("Pais em analise (B/I)? ").upper()

idade_minimaB = 18
idade_minimaI = 17
idade = 2023 - ano_nasc

#Aptidao 
aptB = idade - idade_minimaB 
aptI = idade - idade_minimaI
inpB = idade_minimaB - idade
inpI = idade_minimaI - idade 

if ((pais == "B") and (idade >= 18)):
	print ("sim")
	print (aptB)

elif ((pais == "I") and (idade >= 17)):
	print("sim")
	print(aptI)

elif ((pais == "I") and (idade < 17)):
	print ("nao")
	print (inpI)
	
elif (pais == "B" and idade < 18):
	print("nao")
	print(inpB)

elif (pais != "B" or pais != "I"):
	print("invalido")