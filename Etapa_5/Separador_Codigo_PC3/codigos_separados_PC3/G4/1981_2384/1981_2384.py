r = input("Resultado do clube: ")
v = input("Quantas vezes alcançou o resultado?")

if(r == "Campeao" and v == "06-vezes"):
	time = "corinthians"
elif(r == "Campeao" and v == "03-vezes"):
	time = "santos"
elif(r == "Vice-Campeao" and v == "01-vez"):
	time = "flamengo"
elif(r == "Vice-Campeao" and v == "06-vezes"):
	time = "internacional"
else:
	time = "TIME DE FUTEBOL NAO IDENTIFICADO"

print(time.upper())
	
