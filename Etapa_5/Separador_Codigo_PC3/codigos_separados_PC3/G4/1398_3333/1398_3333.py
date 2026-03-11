tv = float(input("leia o tempo de voo"))
cp1=5000
mp=100*tv
cp2=8000
me=(tv-200)*90
mpp= 100*200
if	(tv <= 200):
	c= cp1+mp
else:
	c= cp2+mpp+me
print(round(c,2))