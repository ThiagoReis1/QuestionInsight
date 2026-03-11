nota1 = float(input("Qual o valor da primeira nota: "))
nota2 = float(input("Qual o valor da segunda nota:" ))
nota3 = float(input("Qual o valor da terceira nota:" ))
valor_media = (nota1 + nota2 + nota3)/3
print(round(valor_media, 1))
if (valor_media >= 7):
	print("Aprovado")
else:
	print("Reprovado")