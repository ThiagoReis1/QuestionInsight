from numpy import *
x = array(eval(input("Insira notas:")))
i = 0
n = 0
a = 0
while i<size(x):
	if x[i]>=0:
		n = n + (i+1)*x[i]
		a = a + (i+1)
	i = i+1
print(round(n/a,2))
	