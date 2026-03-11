unid=input("Centimetros ou Polegadas (C/P): ")
if (unid.upper()=="C"):
	cen=float(input("Quantos Centimetros deseja converter? "))
	pol=0.393701*cen
	val=pol
else:
	pol=float(input("Quantas Polegadas deseja converter? "))
	cen=pol/0.393701
	val=cen
print(round(val,2))