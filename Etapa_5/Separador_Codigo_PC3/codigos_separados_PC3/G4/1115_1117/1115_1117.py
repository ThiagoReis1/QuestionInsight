X=float(input())
Y=int(input())
print("Entradas: R$", round(X, 2),"e codigo",Y)
if X<0 and Y<101 or Y>104:
	print("Dado invalido")
else:
	if Y==101:
		print("Novo salario: R$",round(X*0.0080+X, 2))
	elif Y==102:
		print("Novo salario: R$",round(X*0.0065+X, 2))
	elif Y==103:
		print("Novo salario: R$",round(X*0.0060+X, 2))
	else:
		print("Novo salario: R$",round(X*0.0055+X, 2))