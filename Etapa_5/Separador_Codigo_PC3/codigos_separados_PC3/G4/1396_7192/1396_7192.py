consumido= float(input("valor consumido: "))
x= 10/100
y= 6/100


if (consumido <= 300):
   v= consumido +( x*consumido)
	
else:
	consumido > 300
	v= consumido + ( y*consumido)
	
print(round(v,2))
