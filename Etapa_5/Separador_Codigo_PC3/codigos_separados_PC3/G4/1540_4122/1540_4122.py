from math import*
x=eval(input("angulo x"))
k=int(input("quantidade de termos"))
sinal=1
c=0
i=1
while(k>i):
	c=c+((x**i)*sinal/factorial(i*2))
	sinal=sinal*(-1)
	i=1+i
print(round(1-c,6))