
cont = 0

num = int(input())
while(num >= 0):
	if((num >= 26) and (num <= 85)):
		cont = cont + 1
	
	num = int(input())
	
print(cont)