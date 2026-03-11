x= float(input("primeira nota:"))
y= float(input("segunda nota:"))
z= float(input("terceira nota:"))
w= float(input("quarta nota:"))
a= (x+y+z+w)/4
print(round(a,2))
if( a >= 7.0):
	print("Aprovado")
else:
	print("Reprovado")