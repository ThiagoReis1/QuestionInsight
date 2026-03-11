x=int(input("votos1: "))
y=int(input("votos2: "))
if(x>y and x>0 and y>0 and x!=y ):
	m="Ambrosio Rutra"
	v=x/100
else:
	m="Demelza Olecram "
	v=y/100
print(m)
print(round(v,2))