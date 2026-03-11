p = int(input("Movimento: "))
som = 0

while(p != 0):
	som = som + p
	p = int(input("Movimento: "))

print(som)

if(som > 0 ):
	print("Direita")
	
elif(som == 0):
	print("Inicial")
	
else: 
	print("Esquerda")