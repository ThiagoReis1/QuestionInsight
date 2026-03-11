from numpy import *
n = array(eval(input("digite aqui: ")))
v = 0
d =  0

while d < size(n):
	if n[d] == 1:
		v = v + 10 
	elif n[d] == 2:
		v = v + 5
	elif n[d] == 3:
		v = v + 0
	elif n[d] == 4:
		v = v + 5
	elif n[d] == 5:
		v = v + 20
	elif n[d] == 6:
		v = v + 10
	d+=1
print(v)
