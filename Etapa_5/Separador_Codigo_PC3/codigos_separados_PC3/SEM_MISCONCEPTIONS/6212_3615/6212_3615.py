entrada = int(input())
cont = 0
while entrada != -1:
	if entrada > 25 and entrada <= 85:
		cont +=1
	entrada = int(input())
print(cont)