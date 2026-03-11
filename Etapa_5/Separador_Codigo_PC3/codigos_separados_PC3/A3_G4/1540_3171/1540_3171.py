from math import *

x = eval(input("Informe o angulo em radianos: "))
k = int(input("Informe a quantidade de termos: "))

i = 1
t = 2
cos = 0

while(i <= k):
	if(k == 1):
		cos = 1.0
	else:
		cos = cos - (x/(factorial(t)))
		
print(cos + 1)
