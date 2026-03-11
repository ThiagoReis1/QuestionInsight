posInicial = int(input())
velocidade =  int(input())
tempoDes = int(input())

posFinal = posInicial+velocidade*tempoDes
print(posFinal)

if(posFinal > posInicial+1000):
	print('Sim')
else: 
	print('Nao')