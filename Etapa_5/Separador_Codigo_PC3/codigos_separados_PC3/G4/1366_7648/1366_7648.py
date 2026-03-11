from math import radians 
from math import sin 

a = float(input("valor do angulo"))
v = float(input("velo da flecha"))

radians(a)
		  
d = (v**2)*((sin(2 * radians(a))/9.8))
			  
print(round(d,2))		  
			  
			  
				  
				  
				  
