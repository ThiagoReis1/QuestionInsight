from numpy import * 
p = float(input("digite o numero:"))
x = array(eval(input("digite o vetor:")))
y = array(eval(input("digite o vetor:")))
t = p / p - 1
s = 0
for i in range(size(x)):
	s = abs(2 * (x[i]) +  3 *(y[i])) ** t
	d = (s) ** (1/p)
print(round(d, 3))