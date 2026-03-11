#ENTRADA DE DADOS
n1= float(input("n1?"))
n2= float(input("n2?"))
n3= float(input("n3?"))
n4= float(input("n4?"))
n5= float(input("n5?"))

#CALCULO INTERNO
s=n1+n2+n3+n4+n5
m=s/5

#SAIDA DE DADOS
print(round(m,2))
if (m<7):
	print("Reprovacao por nota")
else:
	print("Aprovacao")
