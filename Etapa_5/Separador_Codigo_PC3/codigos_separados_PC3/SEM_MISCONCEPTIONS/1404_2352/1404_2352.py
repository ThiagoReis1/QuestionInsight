nomedacabeca = input("Digite Aameul ou Hethradiah:")
lado1 = input("Digite o valor sorteado:")
lado2 = input("Digite o valor sorteado:")
lado3 = input("Digite o valor sorteado:")

if (nomedacabeca == "Aameul"):
	x = 8 * (lado1 + lado2 + lado3)
	
else:
	x = 2 * (lado1 + lado2 + lado3)
	
print(x)