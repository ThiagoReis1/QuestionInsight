from numpy import*
n = array(eval(input("insira o vetor com as notas do aluno")))
media = (sum(n) - min(n))/ (size(n) - 1)
print(round(media,2))