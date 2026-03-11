from math import*
grav=9.8
angu=radians(float(input("angu:")))
d=float(input("d:"))
v=sqrt(d*(grav/sin(2*angu)))	 
print(round(v,2))