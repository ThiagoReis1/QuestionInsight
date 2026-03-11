num = int(input("Digite: "))
qat = 0
num5 = 0

while(num != -1):
	if (num == 5):
	   num5 = num5 + 1
	   qat = qat + 1
	
	elif ((num >= 1) and (num <= 10) and (num != 5)):
		qat = qat + 1
		num5 = num5 + 0
	num = int(input("Dados: "))

eoq = (num5 * 100) / qat

print(qat)
print(round(eoq,2))