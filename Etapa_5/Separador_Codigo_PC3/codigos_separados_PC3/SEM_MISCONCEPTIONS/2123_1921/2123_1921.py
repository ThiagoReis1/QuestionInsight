from numpy import*
notas = array(eval(input("notas do aluno ")))
menor = min(notas)
maior = max(notas)
soma = sum(notas)
media = soma - menor - maior
f = (media + maior)/3.0
if(f >= 5.0):
	print(round(f,2))
	print("aprovou".upper())
else:
	print(round(f,2))
	print("reprovou".upper())