from numpy import*

p = eval(input("numero real:"))
x = array(eval(input("v1")))
y= array(eval(input("v2")))
t = p/(p-1)
i = 0
soma = 0
j = 0
soma2 = 0
while(i<size(x)):
	soma = soma + abs(x[i])**t
	i= i +1
soma= soma**(1/t)
while(j<size(y)):
	soma2 = soma2 + abs(y[i])**t
	j= j +1
soma2 = soma2**(1/t)

n = soma - soma2

print(round(n,4))


	

