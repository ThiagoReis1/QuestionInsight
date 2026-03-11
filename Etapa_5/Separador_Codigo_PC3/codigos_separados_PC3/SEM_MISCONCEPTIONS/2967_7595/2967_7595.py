minha_altura = float(input("Digite a sua altura: "))
altura_amigo = float(input("Digite a altura do seu amigo: "))

maior_altura = max(minha_altura,altura_amigo)

if(maior_altura >= 1.37):
	print("Sim")
	print(maior_altura)
else: 
	print("Nao")
	print(maior_altura)