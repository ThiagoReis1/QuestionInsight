from numpy import*
p= input("").upper()
v=0
i=0
d=0
s=0
j=0

while i < len(p):
	if p[i]=="B":
		d = d + 1
	elif p[i] == "C":
		s = s + 1
	elif p[i] == "E":
		j = j + 1
		
	i=i + 1
v= d*3.75+ s*7.90+ j*9.85
print(round(v,2))