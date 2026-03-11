altura_macaco = 1.4
taxa_macaco = 0.06
altura_leao= float(input("insira a altura:"))
taxa_leao= float(input("insira a taxa:"))

anos= 0

while altura_macaco < altura_leao:
	altura_macaco= altura_macaco + taxa_macaco
	altura_leao= altura_leao + taxa_leao
	anos= anos + 1
	
print(anos)
	