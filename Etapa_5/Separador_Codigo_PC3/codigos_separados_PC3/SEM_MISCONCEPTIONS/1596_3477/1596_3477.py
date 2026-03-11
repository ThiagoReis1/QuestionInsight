from numpy import*
notas = array(eval(input("digite a nota : ")))
media = (sum(notas) - min(notas)) / (size(notas)-1)
print(round(media,2))