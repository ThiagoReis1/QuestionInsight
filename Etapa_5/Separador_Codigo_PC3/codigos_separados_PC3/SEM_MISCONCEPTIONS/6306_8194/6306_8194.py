from numpy import*
v = input("Helpmeeee: ")
			 
i = 0
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
		
while(i < len(v)):
	if v[i] == "A":
			 cont = cont + 19.90
			 cont3 = cont3 +1
	if v[i] == "L":
			 cont1 = cont1 + 3.50
			 cont4 = cont4 + 1
	if v[i] == "P":
			 cont2 = cont2 + 4.25
			 cont5 = cont5 + 1
	i = i + 1
val = round(cont+cont1+cont2,2)
print(val, cont3 , cont4, cont5)