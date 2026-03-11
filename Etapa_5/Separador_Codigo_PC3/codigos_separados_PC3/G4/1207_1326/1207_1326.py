from numpy import*
j=eval(input())

i=0
q=0
r=98.48

while i<size(j):
	if j[i]>r:
		q+=1
	i+=1
print(r)
print(q)
