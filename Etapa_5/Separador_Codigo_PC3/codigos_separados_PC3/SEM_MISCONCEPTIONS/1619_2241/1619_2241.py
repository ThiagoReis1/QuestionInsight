from numpy import*

v1= array(eval(input()))
v2= array(eval(input()))

i=0
gc1 = 0
gc2 = 0
gc3 = 0

while i < size(v1):
	if v2[i] == "MORNO":
		gc1 = gc1+45*(v1[i])
		i = i + 1
	elif v2[i] == "QUENTE":
		gc2 = gc2 + 90*(v1[i])
		i= i + 1
	else:
		v2[i] == "FRIO":
		gc3 = gc3 + 0*(v1[i])
		i = i 
print(round((gc1 + gc2 + gc3),2))
		



