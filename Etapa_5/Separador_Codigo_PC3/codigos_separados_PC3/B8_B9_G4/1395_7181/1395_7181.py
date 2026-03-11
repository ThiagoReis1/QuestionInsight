vd=float(input("valor das vendas:  "))

if(vd<=1000):
	vc=(vd*0.05)
else:
	if(vd>1000):
		vc=(1000*0.05)+(vd-1000)*0.1

print(round(vc, 2))