x=input("qual o tipo de ataque:")# Cauda ou Cuspe
n=int(input("dado:"))# varia de 1 a 4
nt=int(input("numero de turnos:"))# magia de cura
if(x=='cauda'):
	msg=n*nt
	print(msg)
else:
	msg=2*(n*nt)
	print(msg)