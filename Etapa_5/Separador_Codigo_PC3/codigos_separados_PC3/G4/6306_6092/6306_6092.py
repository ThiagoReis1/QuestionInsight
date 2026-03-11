from numpy import *
s = input("").upper()
i=0
a=0
b=0
c=0
total=0 
while i < len(s):
	if s [i]=='A':
		total += 19.90
		a=a + 1
	if s [i]== 'L':
		total += 3.5
		b =b+1
	if s[i] == 'P':
		total += 4.25
		c= c + 1
	i=i+1

print(round(total,2),a,b,c)
	
	