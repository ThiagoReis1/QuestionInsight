# Victor Lopes Aguiar -     Matrícula - 21551604
# Avaliacao 02

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print (round(media,2))

if (media >= 6):
	print ("Aprovacao")
else:
	print ("Reprovacao")