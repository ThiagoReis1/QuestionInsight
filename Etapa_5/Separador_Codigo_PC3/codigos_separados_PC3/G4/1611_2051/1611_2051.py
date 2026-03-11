
v= input("etiqueta: ").upper()


i=0
x=0
y=0
#custo total de compras:
while (i< len(v)):
	if ((v[i]=='A')or(v[i]=='E')or(v[i]=='I')or(v[i]=='O')or(v[i]=='U')):
		x=x+1
		i=i+1
	else:
		i=i+1
		y=y+1
		
vog= x*0.15
con= y*0.17
total = vog + con
print(round (total,2))