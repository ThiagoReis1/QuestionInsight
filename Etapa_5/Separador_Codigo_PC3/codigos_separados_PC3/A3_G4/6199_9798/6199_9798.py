ac = 1.8
tc = 0.01

a = float(input("Insira a altura: "))
t = float(input("Insira a taxa de crescimento: "))
altura = a
ano = 0
while a <= ac:
	ano = ano + 1
	a = a + t
	ac = ac + tc
print(ano)
