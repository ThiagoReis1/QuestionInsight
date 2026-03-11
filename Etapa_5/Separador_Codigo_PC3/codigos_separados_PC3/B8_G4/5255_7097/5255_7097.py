p=float(input("qual o peso em kg?"))
d=float(input("qual a distancia em km?"))
c=int(input("qual o codigo?"))
p1=25
d1=0.10
if p>0 and d>0 and c>=1 and c<=4:
	if c==1:
		icms=17/100
		pt=((p*p1+d*d1)*(1+icms))
		print(round(pt,2))
	elif c==2:
		icms=17.5/100
		pt=((p*p1+d*d1)*(1+icms))
		print(round(pt,2))
	elif c==3:
		icms=18/100
		pt=((p*p1+d*d1)*(1+icms))
		print(round(pt,2))
	elif c==4:
		icms=20/100
		pt=((p*p1+d*d1)*(1+icms))
		print(round(pt,2))
else:
	print("Dados invalidos")