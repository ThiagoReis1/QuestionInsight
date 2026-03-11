from math import*
x = float(input("x?"))
k = int(input("k?"))
cont = 1
acul = 1
sh = 0
while(cont <= k):
	sh = sh + (x**acul)/factorial(acul)
	acul = acul+2
	cont = cont+1
print(round(sh,9))