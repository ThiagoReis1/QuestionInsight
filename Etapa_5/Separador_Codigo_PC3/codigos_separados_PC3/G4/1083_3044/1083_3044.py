x=float(input("nota1: "))
y=float(input("nota2: "))
z=float(input("nota3: "))
m=(x+y+z)/3
if(m>=6.0):
	me="Aprovacao"
else:
	me="Reprovacao"
print(round(m,2))
print(me)