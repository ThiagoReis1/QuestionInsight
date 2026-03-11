ataque = input("Qual o tipo de ataque: ")
valor1 = int(input("Qual o primeiro valor sorteado: "))
valor2 = int(input("Qual o segundo valor sorteado: "))
valor3 = int(input("Qual o terceiro valor sorteado: "))
valor4 = int(input("Qual o quarto valor sorteado: "))
sorteio1 = (valor1 + 6)
sorteio2 = (valor2 + 6)
sorteio3 = (valor3 + 6)
sorteio4 = (valor4 + 6)
sorteio = 4* (sorteio1 + sorteio2 + sorteio3 +sorteio4)
if (ataque == "espada"):
	print(sorteio1 + sorteio2 + sorteio3 + sorteio4)
else:
	print((valor1 + valor2 + valor3)* valor4)
	