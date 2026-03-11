from numpy import*
p = float(input())
x = array(eval(input()))
y = array(eval(input()))
t = p/(p-1)
z = 2*x + 3*y
n = 0

for i in range(size(z)):
	n += abs(z[i])**t
	
print(round(n**(1/t), 3))