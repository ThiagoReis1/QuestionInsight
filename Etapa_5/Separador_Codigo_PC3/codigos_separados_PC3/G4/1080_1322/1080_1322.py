p1 = float(input("Informe o valor da primeira nota: "))
p2 = float(input("Informe o valor da segunda nota: "))
p3 = float(input("Informe o valor da terceira nota: "))

nota = (p1 + p2 + p3)/3

if(nota >= 5):
	media = "Aprovado"
else:
	media = "Reprovado"
print(round(nota,1), media)