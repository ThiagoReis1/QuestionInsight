gri=int(input("grifos: "))
x=int(input("novos grifos: "))
y=int(input("grifos contaminados: "))

i=0

while (gri>0):
	gri=gri+x
	gri=gri-y
	i=i+1
print(i)