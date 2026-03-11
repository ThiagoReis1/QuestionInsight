altura_luna = 1.65
taxa_luna = 0.02
altura_do_aluno = float(input("digite a altura: "))
taxa_cresc = float(input("digite a taxa de crescimento: "))

ano = 0

while (altura_do_aluno <+ altura_luna):
	altura_luna = 1.65 + (0.02 * ano)
	altura_do_aluno = altura_do_aluno + (taxa_cresc * ano)
	ano = ano + 1
print(ano)
