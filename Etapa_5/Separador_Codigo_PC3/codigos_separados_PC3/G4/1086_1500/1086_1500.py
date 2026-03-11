x= float(input("primeira nota:"))
v= float(input("segunda nota:"))
m= float(input("terceira nota:"))
t= (x+v+m)/3
if (t==7)or(7<t):
	print(round(t,1))
	print("Aprovado")
else:
	print(round(t,1))
	print("Reprovado")