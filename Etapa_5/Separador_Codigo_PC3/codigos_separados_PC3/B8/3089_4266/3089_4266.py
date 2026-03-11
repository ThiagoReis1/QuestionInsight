x = int(input("Digite o numero de seu movimento: "))
total=0

while(x!=0):
	total = total + x
	if(x!=0):
		x = int(input("Digite outro valor para o proximo movimento: "))

print(total)		
if(total==0):
	print("Inicial")
elif(total<0):
	print("Esquerda")
elif(total>0):
	print("Direita")


