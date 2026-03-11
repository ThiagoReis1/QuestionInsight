from math import*
x=float(input("um numero real: "))
k=int(input("um numero inteiro; "))   #quantidade de termos da serie
n=1
e=0
i=0
while i<k :
	e= 1+x+x**k/factorial(i)
	i=i+1
	k=k+2
print(round(e,9))