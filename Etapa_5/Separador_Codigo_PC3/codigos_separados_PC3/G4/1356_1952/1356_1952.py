#Lucas Nascimento EStevam da Silva     Matricula: 21602757
#Trabalho Pratico 1
#Exercicio 1

a = float(input("Estimativa de alunos:")) #Estimativa de alunos por metro quadrado
b = float(input("Base maior:")) #Comprimento da base maior
c = float(input("Base menor:")) #Comprimento da base menor
d = float(input("Altura:")) #Comprimento da altura do trapezio
Area = float(d * (b + c) / 2)
Quantidade = int(a * Area) #Quantidade de alunos que cabe na sala
print(Quantidade,)