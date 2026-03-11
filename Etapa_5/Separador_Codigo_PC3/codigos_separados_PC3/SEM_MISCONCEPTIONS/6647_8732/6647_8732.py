from numpy import * 
notas = array(eval(input("Notas: ")))
peso = array(eval("2, 1, 5"))
nota1 = notas[0] * peso[0]
nota2 = notas[-2] * peso[-2]
nota3 = notas[-1] * peso[-1]
media = (nota1+nota2+nota3) / 8
print(round(media, 2))