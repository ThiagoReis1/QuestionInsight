# faça seu código aqui!
d=int(input("numero de diarias:"))
v=175*d
if(d<15):
	t=v+20
elif(d==15):
	t=v+16
else:
	t=v+10
print(t)