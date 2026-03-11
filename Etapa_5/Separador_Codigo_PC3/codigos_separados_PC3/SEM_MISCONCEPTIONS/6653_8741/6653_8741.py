from numpy import*
notas = array(eval(input("notas: ")))
peso = array(eval("[3,5,1]"))
nota1 = notas[0] * peso[0]
nota2 = notas[-1] * peso[-1]
nota3 = notas[-2] * peso[-2]
media = (nota1+nota2+nota3) / (9)
print(round(media, 2))