from numpy import*
notas = array(eval(input("Notas: ")))

media = (sum(notas) - min(notas))/ (size(notas)-1)

print(round(media,2))