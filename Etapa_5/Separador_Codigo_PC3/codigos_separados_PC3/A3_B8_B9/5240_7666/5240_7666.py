used = int(input())
valor = 0
if(used < 100):
	valor = used/2
elif(used < 250):
	valor = used*0.75
elif(used < 500):
	valor = used
elif(used >= 500):
	valor = used*1.25
	
print(round(valor + 50,2))