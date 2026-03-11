from numpy import*

notas = array(eval(input("notas: ")))
peso = array(eval("[3,2,4,1,3]"))

nota1 = notas[0] * peso[0]
nota2 = notas[-4] * peso[-4]
nota3 = notas[-3] * peso[-3]
nota4 = notas[-2] * peso[-2]
nota5 = notas[-1] * peso[-1]

media = (nota1 + nota2 + nota3 + nota4 + nota5) / sum(peso)
print(round(media,2))