from numpy import*
notas = array(eval(input("Digite os valores das notas do aluno: "))) #-----> Vetor de notas do aluno
size(notas)
sum(notas)
media = (sum(notas) - min(notas))/(size(notas) - 1)
print(round(media, 2))

#soma = 1.5 + 4.2 + 9.1 = 14.8 ----- 14.8 - 1.5 = 13.3
#size = 3

