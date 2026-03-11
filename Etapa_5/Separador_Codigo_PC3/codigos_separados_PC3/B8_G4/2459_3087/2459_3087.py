p=float(input("peso:"))
d= float(input("distancia: "))
c= int(input("codigo: "))

if c==1: 
	i=17
elif c==2:
	i=17.5
elif c==3:
	i=18
elif c==4:
	i=20

		
s= ((p* 25) + (d* 0.10)) *(1+ (i/100))
print(round(s,2))