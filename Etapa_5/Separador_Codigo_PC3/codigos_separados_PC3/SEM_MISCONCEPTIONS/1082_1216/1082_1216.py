nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))
media_total = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(round(media_total, 1))
if (media_total >= 5.0):
    print("Aprovado")
else:
    print("Reprovado")
	
