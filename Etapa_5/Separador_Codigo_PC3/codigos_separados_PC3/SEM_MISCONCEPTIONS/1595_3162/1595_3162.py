from numpy import*

vetor = array(eval(input("Digite as notas: ")))
tamanho = (size(vetor) - 1)
media = (sum(vetor) - min(vetor))/tamanho

print(round(media, 2))
