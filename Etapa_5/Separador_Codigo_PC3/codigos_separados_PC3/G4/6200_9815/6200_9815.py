ax = float(input("Insira a Altura do outro Aluno: "))
tx = float(input("Insira a Taxa de Crescimento do outro Aluno: "))
am = 1.75
tm = 0.01

ano = 0

while ax < am:
	ano += 1
	am += tm
	ax += tx

print(ano)
	