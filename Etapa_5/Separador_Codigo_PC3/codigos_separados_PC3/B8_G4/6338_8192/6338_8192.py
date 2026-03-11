from numpy import*
n = eval(input("digite um numero?: "))
n1 = int(input("digite o valor?: "))


i = 0
cont = 0
while ( i < (size(n))):
	if (n[i] == n1):
		print(i)
	elif (n[i] > n1):
		cont = cont + 1
	i = i + 1
print(cont)