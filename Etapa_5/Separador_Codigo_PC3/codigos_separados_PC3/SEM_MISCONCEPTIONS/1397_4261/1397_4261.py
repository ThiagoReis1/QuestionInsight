fertilizantes = float(input("qual a area de plantacao?: "))
if(fertilizantes<=10000):
	mensagem=(fertilizantes*5)
else:	
	mensagem =(10000*5 + 4*(fertilizantes-10000))
print(round(mensagem,2))	