q= float(input("Digite a quantidade de combustivel comum: "))
if q<17.5 :
	t= q+0.8
elif q>=17.5 and q<=35:
	t= q+1.3
elif q>35 and q<=50:
	t= q+2.1
elif q>=50:
	t= q+3
print(round(t,1))
