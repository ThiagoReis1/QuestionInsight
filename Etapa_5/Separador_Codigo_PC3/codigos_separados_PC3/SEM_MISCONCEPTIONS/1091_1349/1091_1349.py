num=int(input("Digite o numero de 4 algarismos: "))

parcela1=num//100
parcela2=num%100

propriedade=(parcela1+parcela2)**2

print(parcela1)
print(parcela2)

if propriedade==num:
	print(propriedade,"atende a propriedade")

else:
	print(propriedade)