hp=float(input("hp: "))
d1=float(input("dado 1:"))
d2=float(input("dado 2: "))
d3=float(input("dado 3: "))

if(d1>12):
	d1=12
if(d1<1):
	d1=1
if(d2>12):
	d2=12
if(d2<1):
	d2=1
if(d3>12):
	d3=12
if(d3<1):
	d3=1

dmg = 10*(d1+d2+d3)

if((hp-dmg)>0):
	print(round(hp-dmg))
	print("VIVO".upper())
else:
	print("0")
	print("MORTO".upper())