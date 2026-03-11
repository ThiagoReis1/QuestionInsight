from numpy import *
 
x = input( "digite a palavra: ")
i = 0
cont = 0

while (i < len(x)):
	if((x [i] == "A") or (x[i] == "E") or (x[i] == "I") or (x[i] == "O") or (x[i] == "U")):
		cont= cont + 1.12
		
	else: 
		cont = cont + 1.18
	i = i + 1
		
print(round(cont,2))		