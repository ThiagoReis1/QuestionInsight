#LETICIA DANTAS - 21601436

from numpy import*

p = float(input("Insira numero:"))
x = array(eval(input("vetor x: ")))
y = array(eval(input("vetor y: ")))
t = p/(p+1)
l = 0
for i in range(size(x)):
	l = l + ((abs(x[i] - y[i]))**t)
l = l ** (1/t)
print(round(l, 4))