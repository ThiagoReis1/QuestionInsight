from numpy import *

n = array(eval(input("N: ")))
i = 0 
s = 0

while i<size(n):
	if n[i]==1:
		s = s + 10
	elif n[i]==2:
		s = s + 5
	elif n[i]==3:
		s = s
	elif n[i]==4:
		s = s + 5
	elif n[i]==5:
		s = s + 20
	elif n[i]==6:
		s = s + 10
	i = i + 1	
print(s)