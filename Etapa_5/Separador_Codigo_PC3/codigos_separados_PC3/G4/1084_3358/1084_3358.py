n1=float(input("insira nota 1:"))
n2=float(input("insira nota 2:"))
n3=float(input("insira nota 3:"))
n4=float(input("insira nota 4:"))
#calculo media aritmetica
media= (n1+n2+n3+n4)/4
print(round(media, 1))
#imprima se verdadeiro ou falso
if(media >= 6.0):
	print("Aprovado")
else:
   print("Reprovado")
	
	