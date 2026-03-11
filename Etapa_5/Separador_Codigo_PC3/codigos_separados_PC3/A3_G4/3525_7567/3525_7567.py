from math import*
x = float(input(""))
k = int(input(""))
i = 0
soma = 0
senhx = (x)**(2*i+1)/factorial(2*i+1)
while(i < k):
	senhx = (x)**(2*i+1)/factorial(2*i+1)
	i = i + 1
	soma = soma + senhx
print(round(soma, 9))