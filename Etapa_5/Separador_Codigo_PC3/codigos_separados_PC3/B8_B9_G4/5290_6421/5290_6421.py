num= int(input("Digite: "))
quat= 0
num1= 0
while (num != -1):
	if(num == 5):
		num1 = num1+ 1
		quat  = quat+1
		
	elif((num >= 1) and (num <= 10)and (num != 5)):
		quat= quat +1
		num1 = num1 + 0 
	num = int(input("Dados: "))	
	
eoq = (num1 * 100) / quat

print(quat)
print(round(eoq,2))