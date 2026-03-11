n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))
n4 = float(input("Informe a quarta nota:"))

m_arientimetica = (n1 + n2 + n3 + n4)/4

if(m_arientimetica >= 5):
	print(round(m_arientimetica, 2))
	print("Aprovacao")
else:
	print(round(m_arientimetica, 2))
	print("Reprovacao")