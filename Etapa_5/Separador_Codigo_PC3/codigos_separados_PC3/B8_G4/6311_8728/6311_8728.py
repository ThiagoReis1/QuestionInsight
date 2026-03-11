from numpy import*

r = input("dgt").upper()

i = 0 
cont = 0 
c = 0 
e = 0
p = 0 

while i < len(r):
	if r[i] == "C":
		cont = cont + 10.50
		c = c + 1
	elif r[i] == "E":
		cont = cont + 8.75 
		e = e + 1
	elif r[i] == "P":
		cont = cont + 17.90
		p = p + 1 
		
	i = i + 1 
T = round(cont, 2)
print(T, c , e, p)