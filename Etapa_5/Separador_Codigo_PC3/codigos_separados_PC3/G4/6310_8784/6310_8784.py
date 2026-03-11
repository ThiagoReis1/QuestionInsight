from numpy import *
a = input("produto").upper()
cont = 0
m = 0
p = 0
r = 0
i = 0
while i < len(a):
	if a[i] == "M":
	   cont = cont + 7.25
	   m = m+1
	if a[i] == "P":
		cont = cont + 4.75
		p = p+1
	if a[i] == "R":
		cont = cont + 3.50
		r = r+1
	i+=1
print(round(p,2))
					