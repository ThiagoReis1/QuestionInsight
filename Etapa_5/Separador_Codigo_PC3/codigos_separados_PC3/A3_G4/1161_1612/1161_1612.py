z=float(input("zumbis:"))
h=float(input("habitantes"))
x=float(input("zumbis por dia "))
y=float(input("exterminados por dia"))


dia=0
z=0
while z<=h:
	tz=(z-y)*x
	z= z + tz 
	th=(-1)*(z-y)*x
	h= h + th 
	dia= dia + 1
	
	print(h)	