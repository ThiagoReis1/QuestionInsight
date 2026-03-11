from numpy import * 

nota = array(eval(input("insira um conjunto: ")))

peso = [3,2,4,1,3]

v = nota * peso

media = sum(v) / sum(peso)

print(round(media,2))

