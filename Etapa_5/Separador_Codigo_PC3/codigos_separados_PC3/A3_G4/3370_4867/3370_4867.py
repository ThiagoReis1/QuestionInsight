un=input("Unidade(C ou P)?")
v=float(input("Valor da medida?"))
if(un=="C"):
	r=0.393701*v
if(un=="P"):
	r=v/0.393701
print(round(r,2))

