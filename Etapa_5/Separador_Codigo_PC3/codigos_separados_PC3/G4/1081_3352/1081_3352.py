n1= float(input("nota 1:"))
n2= float(input("nota 2:"))
n3= float(input("nota 3:"))
n4= float(input("nota 4:"))

m = (n1+n2+n3+n4)/4
if (m>=5):
	mensagem= "Aprovacao"
else:
	mensagem= "Reprovacao"
		
print(round(m,2),mensagem)