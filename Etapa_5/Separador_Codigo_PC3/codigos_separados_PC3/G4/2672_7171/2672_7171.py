# Area de figuras planas

from math import*

r= float( input( "Digite o raio do poligono:"))
l= int( input( "Digite o numero de lados do poligono:"))

a= 1/2 * ((r* cos( pi/ l))**2 * tan( pi/ l))
			 
print( round( a, 2))			 