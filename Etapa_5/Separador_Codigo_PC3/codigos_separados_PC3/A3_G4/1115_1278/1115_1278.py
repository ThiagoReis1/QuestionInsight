x = float(input())
y = int(input())
print ("Entradas: R$",x,"e codigo",y)
if(x>0) and (y==101 or y==102 or y==103 or y==104):
	if (y==101):
		z = x*0.008 + x
	if (y==102):
		z = x*0.0065 + x
	if (y==103):
		z = x*0.006 + x
	if (y==104):
		z = x*0.0055 + x
	print ("Novo salario: R$",round(z,2))
else:
	print ("Dados invalidos")