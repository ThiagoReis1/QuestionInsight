ataque=input("Digite o ataque desejado (espada/cauda): ")
d1=int(input("Digite o valor de a: "))
d2=int(input("Digite o valor de b: "))
d3=int(input("Digite o valor de c: "))
d4=int(input("Digite o valor de d: "))

if(ataque.lower()=="espada"):
	x=d1+6+d2+6+d3+6+d4+6
	print(x)
else:
	y=(d1+d2+d3)*d4
	print(y)