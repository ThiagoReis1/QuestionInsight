from math import*
p = eval(input("numero chato:"))
k = int(input("numero de constantes:"))
i = 0
sinal = 1
#Qf = (sinal*(p**i))/(factorial(i))
f = 0
while(i<k):
	f = f  + sinal*(p**(2*i))/(factorial(2*i))
	i = i+1
	sinal = -1*sinal
print(round(f,10))
