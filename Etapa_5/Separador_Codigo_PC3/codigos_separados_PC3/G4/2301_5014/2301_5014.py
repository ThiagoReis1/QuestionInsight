import math

b = float(input("Determino o lado b: "));
c = float(input("Determino o lado c: "));

alfa = float(input("Determino o valor do angulo bc: "));

a = ((b**2)+(c**2) - 2*b*c*math.cos(math.radians(alfa)))**0.5;
	  
print(round(a, 2));
	 
	
