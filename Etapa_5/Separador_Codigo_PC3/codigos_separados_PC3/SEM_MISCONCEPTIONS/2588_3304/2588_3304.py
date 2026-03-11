from numpy import*

v = array(eval(input("")))

limvel = v[0]
liminf = limvel + (limvel * 0.20)
limsup = limvel + (limvel * 0.50)

a = 0

for i in range(size(v)):
	if(v[i]>liminf and v[i]<limsup):
		print(i)
		a=a+1
print(a)

	