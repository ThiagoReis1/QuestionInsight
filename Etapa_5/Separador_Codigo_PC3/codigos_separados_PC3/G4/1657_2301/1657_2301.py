from numpy import*
s= input()
s= s.split(',')
a= 0
b= 0
c= 0
d= 0
e= 0 
for i in s:
	if i == "AZ":
	   a = a+1
	elif i == "CA":
		b = b+1
	elif i == "FL":
		c = c+1
	elif i == "PA":
		d = d+1
	else:
		e= e+1
		
v2= zeros(5, dtype = int)
v2[0] = a
v2[1]= b
v2[2]= c
v2[3] = d
v2[4]= e

print(max(v2))
print(v2)