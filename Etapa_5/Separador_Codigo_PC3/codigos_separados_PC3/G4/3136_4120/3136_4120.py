from numpy import *


v = array(eval(input("Digite numeros reais positivos: ")))
n = size(v)
i = 0
while(i < size(v)):
	i = i + 1
a = sum(log(v[i] +1))

m = exp(a/n)

print(round(m, n))
