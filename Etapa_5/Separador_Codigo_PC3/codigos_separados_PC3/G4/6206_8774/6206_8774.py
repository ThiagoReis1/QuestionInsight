cont= 0
num= float(input())

while num != -1:
	if num >= 0 and num <= 25:
		cont +=1
	num = float(input())
	
print(cont)