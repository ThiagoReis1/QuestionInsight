precoingresso=float(input("Insira o preco do valor integral do ingresso: "))
total=float(input("Insira a quantidade de ingressos: "))
desconto=19.41
precopromocional=precoingresso-(precoingresso*(desconto/100))

z=(precoingresso+total+(precopromocional-desconto))*2

print(round(z,2))
