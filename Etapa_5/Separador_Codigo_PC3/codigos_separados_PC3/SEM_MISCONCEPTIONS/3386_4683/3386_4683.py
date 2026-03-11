escala=input("escala:")
valor=float(input("valor:"))

if(escala=="R"):
	mensagem=valor/0.0174533
	
	print(round(mensagem,2))

else:
	mensagem=valor*0.0174533
	
	print(round(mensagem,2))