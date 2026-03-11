from math import*

angulo = eval(input("angulo: "))
k = int(input("k: "))
#variavel contadora
count = 1
#variavel acumuladora
sen = 0

exp = 3
sinal = -1
while (count <= k):
	if(count == 1):
		sen = angulo
	else:
		if(sinal > 0):
			sen = sen + (pow(angulo,exp) / (factorial(exp)))
		else:
			sen = sen - (pow(angulo,exp) / (factorial(exp)))
		sinal = sinal *-1
		exp = exp + 2
	count = count + 1
	print(round(sen,10))