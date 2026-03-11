x = 3.75
y = 7.90
z = 9.85
B = 0
C = 0
E = 0
n = 0
pe = input("comprados: ").upper()
i = 0
while (i < len(pe)): 
	if(pe[i]== "B"):
		n= n +  x
		B = B + 1
	elif (pe[i]== "C"):
		n = n + y
		C = C + 1
	elif (pe[i]== "E"):
		n = n + z
		E = E + 1
	i = i + 1
	
print(round(n , 2), B,C,E)