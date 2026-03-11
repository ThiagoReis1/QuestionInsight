p1=float(input())
p2=float(input())
p3=float(input())
p4=float(input())
p5=float(input())

#calcular a media aritmetico (va)
va=(p1+p2+p3+p4+p5)/5
#opcoes
if(va>=7):
	print(round(va, 2))
	print("Aprovacao")
else:
	print(round(va, 2))
	print("Reprovacao por nota")
  