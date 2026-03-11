soma = 0
for i in range(0,5):
	nota = float(input("Nota:"))
	soma +=nota
media = soma/5
print(round(media,1))
if(media >= 5.0):
	print("Aprovado")
else:
	print("Reprovado")