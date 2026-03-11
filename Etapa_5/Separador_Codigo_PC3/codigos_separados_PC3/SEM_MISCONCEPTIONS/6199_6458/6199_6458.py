altura_cicero = 1.8
taxa_cicero = 0.01

alt_pe = float(input("qual a sua altura: "))
taxa_pe = float(input("qual a taxa de crescimento: "))

x = 0

while altura_cicero > alt_pe:
	altura_cicero = altura_cicero + taxa_cicero
	alt_pe = alt_pe + taxa_pe
	x+=1
print(x)