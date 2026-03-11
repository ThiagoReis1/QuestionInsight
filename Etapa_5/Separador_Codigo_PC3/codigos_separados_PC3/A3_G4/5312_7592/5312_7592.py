numB = int(input())
numH = int(input())

PC = 2/100
cont = 0
i = 0

while(cont<numH):
	a = numB * PC
	numB = int(numB + a)
	cont += + 1
print(numB)