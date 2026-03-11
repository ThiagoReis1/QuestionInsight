Vc=float(input("Valor consumido"))
r=0.1*Vc
s=0.06*Vc
Vg=Vc+s
Vt=Vc+r

if(Vc<=300.00):	
	print(round(Vt,2))
if(Vc>300.00):	
	print(round(Vg,2))
	
	