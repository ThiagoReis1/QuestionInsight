#n virus
#n leuc 2 = n vurys
#virus mult
#n leu mult
#quantos dias
v=float(input("numero de virus"))
l=float(input("numero leucocitos"))
tv=float(input("taca mult virus"))
tl=float(input("taxa mult leucocitos"))
tv1=tv/100
tl2=tl/100
t=1
while (v>=2*l):
	v=v+v*tv1
	l=l+l*tl2
	t=t+1
print(t)	

		
		
