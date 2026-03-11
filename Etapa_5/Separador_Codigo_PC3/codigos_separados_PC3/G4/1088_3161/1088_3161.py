a= float(input("insira a nota da prova 1: "))
b= float(input("insira a nota da prova 2: "))
c= float(input("insira a nota da prova 3: "))
d= float(input("insira a nota da prova 4: "))
e= float(input("insira a nota da prova 5: "))
resultado= (a + b + c + d + e)/5
print(round(resultado, 2 ))
if(resultado >= 7):
	print("Aprovacao")
else:
	print("Reprovacao por nota")