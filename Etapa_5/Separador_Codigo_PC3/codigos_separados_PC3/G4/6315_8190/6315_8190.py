from numpy import*

v = input(" string ")

i=0
p=0
p1=0
p2=0
p3=0

while( i < len(v)):
	if(v[i] == "I"):
		p = p+3.75
		p1=p1+1
	if(v[i] == "M"):
		p = p+4.50
		p2=p2+1
	if(v[i] == "S"):
		p = p+2.90
		p3=p3+1
	i = i + 1
print(round(p,2), p1, p2, p3)
