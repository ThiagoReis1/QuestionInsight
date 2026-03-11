cont = 0

entrada = int(input())

while entrada != -1 :
	if entrada >= 26 and entrada <= 50:
		cont+=1
		
	entrada = int(input())
		
print(cont)