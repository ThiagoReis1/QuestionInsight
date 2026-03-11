from math import*
inf=abs(int(input("quantidade: ")))
cal=abs(int(input("quantidade: ")))
Pinf=float(input("quantidade: "))
Pcal=float(input("quantidade: "))

Tinf=inf
Tcal=cal
m=0
while(Tinf+Tcal<50000):
	Tinf=Tinf+(Tinf*Pinf/100)
	Tcal=Tcal+(Tcal*Pcal/100)
	m=m+1
	
print(m)