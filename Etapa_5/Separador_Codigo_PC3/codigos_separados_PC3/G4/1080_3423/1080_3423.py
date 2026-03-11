n1= float(input("nota 1: "))
n2= float(input("nota 2: "))
n3= float(input("nota 3: "))

m= (n1+n2+n3)/3

if m >= 5.0:
	msg= "Aprovado"
else:
	msg= "Reprovado"

print(round(m,1))
print(msg)