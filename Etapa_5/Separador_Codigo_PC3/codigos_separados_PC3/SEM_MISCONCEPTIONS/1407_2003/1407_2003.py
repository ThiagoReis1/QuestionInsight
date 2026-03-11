inicio = int(input("Digite seus pontos de vida: "))  #quantidade de pontos de vida no inicio
dado_1 = int(input("Insira o valor obtido no primeiro dado: "))
dado_2 = int(input("Insira o valor obtido no segundo dado: "))
dado_3 = int(input("Insira o valor obtido no terceiro dado: "))

perdidos = 10*(dado_1 + dado_2 + dado_3)  #quantidade de pontos perdidos

fim = (inicio - perdidos)  #pontos de vida restante

if fim > 0:
	print(fim)
	print("VIVO")
	
else:
	print(0)
	print("MORTO")