p1=float(input("digite a 1 prova: "))
p2=float(input("digite a 2 prova: "))
p3=float(input("digite a 3 prova: "))
vm=(p1+p2+p3)/3
if(vm>=6):
	print(round(vm, 2))
	print("Aprovacao")
else:
	print(round(vm, 2))
	print("Reprovacao")