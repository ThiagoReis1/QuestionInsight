coelhaltura= float(input("diigite a altura do coelho: "))
taxa= float(input("digite a taxa de altura: "))
alturamacaco = 1.86
taxa_macaco = 0.01
anos= 0

while (coelhaltura <= alturamacaco):
	coelhaltura= coelhaltura + taxa
	alturamacaco= alturamacaco + taxa_macaco
	anos= anos + 1
print(anos)