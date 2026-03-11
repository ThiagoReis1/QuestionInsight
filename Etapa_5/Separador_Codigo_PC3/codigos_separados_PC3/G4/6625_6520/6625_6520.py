from numpy import*

v=input("digite a string: ").upper()

c=0
i=0

while (i < len(v)):
	if (v[i] == "B"):
		c=c+1
i=i+1
print(c)