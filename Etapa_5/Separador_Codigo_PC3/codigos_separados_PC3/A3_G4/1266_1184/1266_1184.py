from numpy import*

x = array(eval(input(" vetor 1:")))
y = array(eval(input(" vetor 2:")))

p = float(input("numero:"))

q = p/(p-1)
xq = 0
yq = 0

for ind in range(size(x)):
	if (p > 1):
		xq = (abs(x[0]**q)+ abs(x[2])**q)**1/q
		yq = (abs(y[0]**q)+ abs(y[2])**q)**1/q
		soma = (2*x)-y
print(round(soma, 4))						  