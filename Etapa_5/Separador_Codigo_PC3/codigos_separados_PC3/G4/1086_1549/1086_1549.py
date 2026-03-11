n1 = float(input("digite a nota 1: "))
n2 = float(input("digite a nota 2: "))
n3 = float(input("digite a nota 3: "))

n_media = round((n1 + n2 + n3) / 3, 1)

print(n_media)

if(n_media >= 7):
   print("Aprovado")
else:
	print("Reprovado")