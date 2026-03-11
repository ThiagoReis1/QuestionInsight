ent  = input(" Unid: ")
v = float(input("valor: "))


if( ent == "R"):
	
	gr = v/0.0174533
	r = gr
	
if (ent == "G"):
	rad = 0.0174533*v
	r = rad
	
print(round(r , 2 ))