from numpy import*

d= array(eval( input()))

i= 0
s=0

while i < size(d):
	if d[i] == 1:
		s= s + 10
	elif d[i] == 2:
		s= s + 5
	elif d[i] == 3:
		s= s + 0
	elif d[i] == 4:
		s= s + 5
	elif d[i] == 5:
		s= s + 20
	elif d[i] == 6:
		s= s+ 10
	i= i + 1
print(s)

