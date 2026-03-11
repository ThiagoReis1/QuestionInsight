q=int(input())

if q<17.5:
	valor= q+10.5
	print(round(valor,1))
elif q>=17.5 and q<=35:
	valor= q+14.0
	print(round(valor, 1))
elif q>35 and q<50:
	valor=q+18.6
	print(round(valor,1))
elif q>=50:
	valor=q+24.5
	print(round(valor,1))