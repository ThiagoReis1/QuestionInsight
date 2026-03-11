n1= float(input("Valor da nota 1: "))
n2= float(input("Valor da nota 2: "))
n3= float(input("Valor da nota 3: "))
n4= float(input("Valor da nota 4: "))

m_a= (n1 + n2 + n3 + n4) / 4

if(m_a >= 5.0):
	print(round(m_a, 2))
	print("Aprovacao")
else:
	print(round(m_a, 2))
	print("Reprovacao")