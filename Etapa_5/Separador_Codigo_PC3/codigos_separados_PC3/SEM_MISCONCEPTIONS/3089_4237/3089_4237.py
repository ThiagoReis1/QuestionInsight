partida = int(input("numero inicial: "))

i = 0
total = 0
while(partida != 0): 
	total = total + partida 
	i = i+1
	partida = int(input("Caralho: ")) 
	
if(total<0):
	print(total)
	print("Esquerda")
if(total>0):
	print(total)
	print("Direita")
if(total==0):
	print(total)
	print("Inicial")