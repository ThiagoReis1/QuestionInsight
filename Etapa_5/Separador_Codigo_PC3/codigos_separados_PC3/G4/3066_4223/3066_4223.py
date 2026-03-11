a=int(input("Digite a quantidade incial de pontos de vida: "))
v1=int(input("Digite o primeiro valor sorteado: "))
v2=int(input("Digite o segundo valor sorteado: "))
v3=int(input("Digite o terceiro valor sorteado: "))

if(a-(v1+v2+v3)*10==-40):
	print(0)
	print("morto".upper())
elif(v1<1 and v2<1 and v3<1 or v1>12 and v2>12 and v3>12):
	print("Entrada invalida")
else:
	print("vivo".upper())