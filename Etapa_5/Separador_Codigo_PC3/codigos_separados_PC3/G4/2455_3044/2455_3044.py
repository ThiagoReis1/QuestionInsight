x=int(input("nivel: "))
y=float(input("horas: "))
if(x==1):
	m=y*12
	print(round(m,2))
elif(x==2):
	m=y*17
	print(round(m,2))
else:
	m=y*25
	print(round(m,2))