from numpy import*

nota = array(eval(input()))
peso = array([2, 2, 6, 1])

num = nota * peso

media = sum(num) / sum(peso)
print(round(media, 2))
