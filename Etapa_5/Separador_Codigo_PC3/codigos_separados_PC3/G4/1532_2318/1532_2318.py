from math import*
x =float(eval(input("digite x:")))
k =int((input("digite:")))
sen=0
cont=0
j=1
n=1
while cont<k:
	j=j*(1)
	sen = sen+((x**n)/factorial(n))*j
	n=n+2
	cont=cont+1
print(round(sen,9))