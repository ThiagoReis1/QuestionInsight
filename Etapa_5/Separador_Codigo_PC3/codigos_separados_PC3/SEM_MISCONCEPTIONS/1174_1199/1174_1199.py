N = int(input("Insira um numero: "))
numerador = 1
numexp = 3 
den1 = 9
den2 = 3
sinal = 1
x = 0.0
count = 1

while (N >= count):
	x = x + (sinal*(-numerador**numexp)/den1 + den2)
	numerador = numerador + 1
	den2 = den2 + 2
	sinal = sinal *(-1)
	count = count + 1
	
 

 
print (round(x,8))