from math import * 

c= float(input("consumo:")) 


vf= (0.28 * c) + 23
v= vf * 31/100
vt= vf + v 

print(round(vt,2))
		