from numpy import*
a = input("").upper()
c = 0
b = 0
h = 0
f = 0
while(c < len(a)):
	if(a[c] == "C"):
		b = b + 1
	elif(a[c] == "E"):
		h = h + 1
	elif(a[c] == "P"):
		f = f + 1
	c = c + 1
i = 0
cont = 0 
while(i < len(a)):
	if(a[i] == "C"):
		cont = cont + 10.50
	elif(a[i] == "E"):
		cont = cont + 8.75
	elif(a[i] == "P"):
		cont = cont + 17.90
	i = i + 1

print(round(cont, 2), b, h, f)
	
	