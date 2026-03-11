num = int(input())
cont = 0
while num != -1: 
	if num >= 0  and num <= 25:
		cont +=1
	num = int(input())
	
print(cont)