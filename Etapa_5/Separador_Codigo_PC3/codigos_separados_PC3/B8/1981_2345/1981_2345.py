tipo1=input("resultado do time:")
tipo2=input("quantas vezes o time alcancou o resultado:")

if(tipo1 !="CAMPEAO" or tipo2 !="06-vezes" or tipo2 !="03-vezes" and tipo1!="VICE-CAMPEAO" or tipo2 !="01-vez" or tipo2 !="06-vezes"):
	print("tipo de futebol nao identificado".upper())
else:
	if(tipo1=="CAMPEAO" and tipo2=="06-vezes"):
		print ("corinthians".upper())
	elif(tipo1=="CAMPEAO" and tipo2=="03-vezes"):
		print ("santos".upper())
	elif (tipo1=="VICE-CAMPEAO" and tipo2=="01-vez"):
		print("flamengo".upper())
	elif (tipo1=="VICE-CAMPEAO" and tipo2=="06-vezes"):
		print ("internacional".upper)