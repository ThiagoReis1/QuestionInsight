from numpy import*
n = array(eval(input()))
p = [4,3]
i = 0
x = 0
m = 0
while i< size(n):
	x = x+(n[i]*p[i])
	m = m +p[i]
	i+=1
t = x/m
print(round(t, 2))