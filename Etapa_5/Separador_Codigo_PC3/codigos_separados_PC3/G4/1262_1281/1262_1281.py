from numpy import *
p=eval(input("numero real maior que 1"))
x=array(eval(input("vetor x")))
y=array(eval(input("vetor y")))
t=(p)/(p-1)
n=0
j=0
for i in x:
	n=n+(abs(i-y[j])**t)
	j=j+1
v=n**(1/t)
print(round(v, 6))