res=input("Resultado do time: ").upper()
q=input("Quantas vezes esse resultado: ")

if((res!="CAMPEAO" and res!="VICE-CAMPEAO") or(q!="06-vezes" and q!="03-vezes" and q!="01-vez")):
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
elif(res=="CAMPEAO" and q=="06-vezes"):
	print("CORINTHIANS")
elif(res=="CAMPEAO" and q=="03-vezes"):
	print("SANTOS")
elif(res=="VICE-CAMPEAO" and q=="01-vez"):
	print("FLAMENGO")
else:
	print("INTERNACIONAL")