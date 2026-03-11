numX = int(input())
numY = int(input())
cont = numX
soma  = 0

while cont <= numY:
	if cont%3 == 0:
		soma = numX + numY
	cont+=1
print(cont)	
