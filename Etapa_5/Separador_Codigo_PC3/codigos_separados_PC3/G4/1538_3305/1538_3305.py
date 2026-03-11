from math import*
x = eval(input("entre com o numero real:"))
k = int(input("entre com a quantidade de termos da serie:"))
cont = 0
i = 1
tg = x
while(cont<k):
	tg = tg + ((-1)**(cont)) * ((x**i)/ factorial(i))
	cont = cont + 1
	i = i + 2
print(round(tg, 8))