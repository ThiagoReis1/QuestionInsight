from numpy import*
s=eval(input("diga os saltos:"))

i=0
q=0
r=8.95
while i<size(s):
	if s[i]>r:
		q+=1
	i+=1
print(r)
print(q)