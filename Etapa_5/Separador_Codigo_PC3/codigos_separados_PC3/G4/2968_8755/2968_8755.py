c=input("comida escolhida: ")
qc=int(input("quantidade de comida: "))
qr=int(input("quantidade de refrigerantes: "))
l=5
s=3.50
r=4

if c=="L":
	t=(qc*l)+(qr*r)
	print(round(t,2))
else:
	c=="S"
	t=(qc*s)+(qr*r)
	print(round(t,2))