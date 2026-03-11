from math import*
x = eval(input("DIgite o angulo: "))
k =  int(input("Digite o termo:"))
p = 0
s = 0
e = 0
n = 0
sinal = 1 
while(n < k ):
	a = (x**e)/(factorial(p))*sinal
	sinal = sinal * (-1)
	s = s + a
	p = p + 2
	e = e + 1
	n = n + 1
print(round(s, 6))