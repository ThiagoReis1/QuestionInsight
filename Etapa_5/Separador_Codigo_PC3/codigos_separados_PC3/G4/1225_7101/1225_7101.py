from numpy import*
from math import*
x = array(eval(input("Digite um vetor de numeros reais: ")))
m = sum(x)/size(x)
a = 0
b = size(x)-1
for i in range(size(x)):
	a = a + ((x[i] - m)**2)
d = sqrt(a/b)
print(round(d,3))