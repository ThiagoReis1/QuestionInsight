nota1 = float(input("Digite a primeira a nota: "))
nota2 = float(input("Digite a segunda a nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a terceira nota: "))

media=(nota1 + nota2 + nota3+ nota4)/4

if media >=5.0:
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
print(round(media,2))
print(mensagem)

	
	
	
	
	
	
	
	