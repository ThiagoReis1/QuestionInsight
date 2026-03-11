#Universidade Federal do Amazonas
#Curso de engenharia de produção
#Matéria: Introdução a ciancia dos computadores
#Aluno: Allan Bezerra - 21552438

a = float(input("Comprimento da fazenda: "))
b = float(input("Largura da fazenda "))
c = float(input("Custo de aplicacao do m2: "))
#Area de aplicacao
A = (a * b) / 2
#Custo do servico
total = A * c
print(round(total,2))