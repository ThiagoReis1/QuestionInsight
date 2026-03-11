n1 = float(input("insira o valor da primeira nota:"))
n2 = float(input("insira o valor da segunda nota:"))
n3 = float(input("insira o valor da terceira nota:"))
n4 = float(input("insira o valor da quarta nota:"))
m = (n1+n2+n3+n4)/4

if (m >=5.0):
	m = round(m,2)
	print (m)
	print ("Aprovacao")
else:
	m = round(m,2)
	print (m)
	print ("Reprovacao")