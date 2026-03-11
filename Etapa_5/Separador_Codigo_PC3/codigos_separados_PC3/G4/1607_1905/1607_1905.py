from numpy import *
x = array(eval(input("Insira um vetor de andares:")))
i = 0
y = []
while i<size(x)-1:
	if x[i+1]-x[i]>0:
		y.append(3*(x[i+1]-x[i]))
	else:
		y.append(-3*(x[i+1]-x[i]))
	i = i+1
print(sum(y))	
