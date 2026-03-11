a=float(input("salario"))
b=int(input("codigo"))
x=float(input("reajuste"))
c=((x*a/100)+a)

if(b=="101"):
	x=0.80
	print("Novo salario: R$ ",(round(c,2)))
	
elif(b=="102"):
	x=0.65
	print("Novo salario: R$ ",(round(c,2)))
elif(b=="103"):
	x=0.60
	print("Novo salario: R$ ",(round(c,2)))
elif(b=="104"):
	x=0.55
	print("Novo salario: R$ ",(round(c,2)))
	
print()	
if(b<101)or(b>104):
	print("Dados invalidos")