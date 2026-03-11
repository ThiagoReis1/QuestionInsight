from numpy import *

v1 = " "
c1 = input("Codigo: ").upper()
i = 0
total = 0


while (i<len(c1)):
	if (v1[i] == 'a' or  v1[i] == 'e' or v1[i] == 'i' or v1[i]== 'o' or v1[i] == 'u'):
		var1 = 25.12
		total = total + (var1*c1)
	else:
		var2 = 40.12
		total = total + (var2*c1)
	i = i + 1
	
total = array(total)
la = sum(total)
print(round(la,2))