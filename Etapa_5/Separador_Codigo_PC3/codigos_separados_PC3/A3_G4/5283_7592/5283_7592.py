a = int(input())

neg = 0
posi = 0
cont = 0

while(a != 0):
	if(a < 0):
		posi += 1
		cont += 1
	
	else:
		neg += 1
		cont += 1  
	a = int(input())
		
soma =  neg/cont * 100

print(cont)
print(round(soma,2))