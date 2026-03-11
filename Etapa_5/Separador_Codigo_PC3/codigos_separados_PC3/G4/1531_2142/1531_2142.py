from math import *
x = eval(input("Ângulo em radianos: "))
k = int(input("Números de termos da série: "))
y = 1
soma = 0
i = 2
fim = k
 
while(i <= fim):
	soma = soma + ((y)**(i-1))*(x**(2*i-1))/factorial(2*i*2)
	y = -y
	i = i + 1
print(round(soma,10))