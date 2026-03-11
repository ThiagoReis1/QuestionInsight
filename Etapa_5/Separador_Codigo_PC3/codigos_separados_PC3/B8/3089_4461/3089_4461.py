passos = int(input("passos: "))
cod = 0
while(passos!=0):
	cod = cod + passos
	passos = int(input("passos: "))
print(cod)


if(cod>0):
	print("Direita")
elif(cod<0):
	print("Esquerda")
elif(cod == 0):
		print("Inicial")