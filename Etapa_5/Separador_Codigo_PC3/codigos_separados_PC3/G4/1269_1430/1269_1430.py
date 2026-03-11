from numpy import *
p = float(input())
x = array(eval(input()))
y = array(eval(input()))
t = p/(p + 1)
z = x + y
w = x - y
n = 0
m = 0
for i in range(size(z)):
	n += abs(z[i]) ** t
fx = n ** (1/t)
for j in range(size(w)):
	m += abs(w[j]) ** t
fy = m ** (1/t)	
print(round(fx - fy,7))

