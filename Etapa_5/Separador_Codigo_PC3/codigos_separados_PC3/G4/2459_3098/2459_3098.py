	#duas casas arredondado
	#3 entradas ver o tipo
peso=float(input("peso do produto"))#inicio das entradas
dist=float(input("distancia do produto"))
cod=float(input("codigo do estado para onde o produto ira ser enviado"))
if(peso>0 and dist>0 and cod==1):
	servico=(peso*25.0 + dist * 0.10) * (1.0 + 0.17)
	print(round(servico,2))
elif(peso>0 and dist>0 and cod==2):
	servico=(peso*25.0 + dist * 0.10) * (1.0 + 0.175)
	print(round(servico,2))
elif(peso>0 and dist>0 and cod==3):
	servico=(peso*25.0 + dist * 0.10) * (1.0 + 0.18)
	print(round(servico,2))
elif(peso>0 and dist>0 and cod==4):
	servico=(peso*25.0 + dist * 0.10) * (1.0 + 0.20)
	print(round(servico,2))
else:
	print("Dados invalidos")