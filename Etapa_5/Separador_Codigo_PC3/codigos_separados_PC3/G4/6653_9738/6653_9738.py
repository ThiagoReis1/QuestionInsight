from numpy import*

n= array(eval(input()))
p= array([3,5,1])

i= 0

media= 0
soma= 0

if size(n) == size(p):
	while i < size(n):
		media= media +(n[i]*p[i])
		soma= soma + p[i]
		i=i + 1
print(round(media/soma,2))