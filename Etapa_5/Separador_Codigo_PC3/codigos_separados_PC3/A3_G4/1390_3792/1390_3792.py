co= float(input("cosumo"))
vc= float(input("valor da conta"))
f= float(input("franquia"))
v1=100*1.20
v2=100*1.40+25
if co == v1:
	p= "limite" 
	
else:
	p= "utrapassado"
	
print(round(p,2)) 	