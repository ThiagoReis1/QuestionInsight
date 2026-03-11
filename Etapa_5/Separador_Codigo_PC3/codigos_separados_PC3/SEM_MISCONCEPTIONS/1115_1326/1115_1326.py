x = float(input("Digite o salário atual: "))
y = float(input("Digite o código: "))
r1 = (x*0.080)
r2 = (x*0.065)
r3 = (x*0.060)
r4 = (x*0.065)

if(y==101):
	print("Entradas:", x , "e codigo", y)
	print("Novo salário:", r1)
elif(y==102):
	print("Entradas:", x , "e codigo", y)
	print("Novo salário:", r2)
elif(y==103):
	print("Entradas:", x , "e codigo", y)
	print("Novo salário", r3)
elif(y==104):
	print("Entradas:", x , "e codigo", y)
	print(round("Novo salario: ", r4 ,2)
else:
	print("Entradas:", x , "e codigo", y)
	print("Dados invalidos")