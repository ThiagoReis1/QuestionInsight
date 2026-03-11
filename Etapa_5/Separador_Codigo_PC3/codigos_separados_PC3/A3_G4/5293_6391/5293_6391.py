#Num = int(input("Digite um numero qualquer: "))
cont = 0

while True:#(Num != 0):
	Num = int(input("Digite: "))
	if(Num == 0):
		break
	cont = cont + 1
	pares = Num % 2 == 0
	i = cont
print(cont)
print(round(i, 2))
		#quant = Num % 2 == 0
		#cont = cont + 1
		#i = (quant * 100) / cont		
	#Num = int(input("Digite um numero qualquer: "))
	#print(cont)
	#print(round(i, 2))