n1 = (float(input("digite a primeira nota: ")))
n2 = (float(input("digite a segunda nota: ")))
n3 = (float(input("digite a terceira nota: ")))
n4 = (float(input("digite a quarta nota: ")))
n5 = (float(input("digite a quinta nota ")))


media = (n1 + n2 + n3 + n4 + n5) / 5


if(media >= 6):
		print(round(media,2))
		print("Aprovado")

else:
		print(round(media,2))
		print("Reprovado")
			

			
