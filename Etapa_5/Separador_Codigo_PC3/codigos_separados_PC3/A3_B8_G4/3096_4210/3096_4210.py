p = 1
i = 0
soma = 0

while(p!=0):
	p = int(input("posicao:"))
	if (p == 1):
		soma = soma + 20
	elif (p ==2 ):
		soma = soma + 15
	elif (p == 3):
		soma = soma + 10
	elif (p>3 and p<=10):
		soma = soma + 11 - p 
	elif(p>10 and  p<0):
		soma = soma + 0
print(soma)