alturamacaco = 1.86
taxamacaco = 0.01

ac = float(input("Digite a altura: "))
tc = float(input("Digite a taxa de crescimento: "))
a = 0
while alturamacaco > ac:

	ac = ac + tc
	alturamacaco= alturamacaco + taxamacaco
	a += 1 
print(a)