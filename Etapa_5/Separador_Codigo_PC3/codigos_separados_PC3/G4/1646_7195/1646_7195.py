from numpy import *
s = array(eval(input("saques:")))

abaixo=0

for i in range (size(s)):
	if s[i]<=50:
		abaixo=abaixo+1
print(abaixo)		
	
pos= zeros(abaixo, dtype=int)
n=0
for i in range (size(s)):
	if s[i]<=50:
		pos[n]=i
		n=n+1
print(pos)

