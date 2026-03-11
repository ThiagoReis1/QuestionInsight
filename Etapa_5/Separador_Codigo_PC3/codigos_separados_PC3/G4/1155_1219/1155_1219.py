nv=int(input("Digite o numero de inicial virus: "))
nl=int(input("Digite o numero de inicial de leucocitos: "))
tv= float(input("Digite a taxa de multiplicaçao do virus: "))
tl= float(input("Digite a taxa de multiplicaçao de leucocitos: "))
i= 0
while (nl)*2<(nv):
	nv=nv+(nv*tv)
	nl=nl+(tl*tl)
	i= i+1
print(i)
	