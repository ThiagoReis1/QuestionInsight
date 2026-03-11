from numpy import *
s= array(eval(input(''))).split('').upper()
v= 'A','E','I','O','U'
i=0
for i in range(size(s)):
	if(i == v):
		cal= s[i]*0.15
	i=i+1
	if(i != v):
		cal=s*0.17
	i=i+1
print(round(cal,2))