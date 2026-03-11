n1 = float(input("digite a nota1: "))
n2 = float(input("digite a nota2: "))
n3 = float(input("digite a nota3: "))
n4 = float(input("digite a nota4: "))
n5 = float(input("digite a nota5: "))

media = ((n1 + n2 + n3 + n4 + n5) / 5)
if( media >= 5.0):
	mensagem = "Aprovado"
else: 
	mensagem = "Reprovado"
	
print(round(media, 1))
print(mensagem)


