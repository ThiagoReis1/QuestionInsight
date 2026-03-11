from math import*
x = float(eval(input("digite x: ")))
k = int((input("digite k: ")))
cos=1
cont=1
j=1
n=2
while cont<k:
	j=j*(-1)
	cos = cos+((x**n)/factorial(n))*j
	n=n+2
	cont=cont+1
print(round(cos,10))
