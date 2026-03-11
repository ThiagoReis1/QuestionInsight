from math import*
b = float(input("Digite um valor"))
c = float(input("Digite um valot"))
alpha = float(input("Determine o angulo"))
angulo = radians(alpha)
a = sqrt((b**2)+(c**2)-(2*b*c)*cos(angulo))
	
print (round(a,2))
