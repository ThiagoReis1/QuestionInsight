nota1=float(input("primeira nota: "))
nota2=float(input("segunda nota: "))
nota3= float(input("terceira nota: "))
nota4= float(input("quarta nota: "))
nota5= float(input("quinta nota: "))

v= round(((nota1 + nota2 + nota3 + nota4 + nota5) / 5),2)
print(v)
if(v>=6.0):
	print("Aprovacao")
else:
	print("Reprovacao")