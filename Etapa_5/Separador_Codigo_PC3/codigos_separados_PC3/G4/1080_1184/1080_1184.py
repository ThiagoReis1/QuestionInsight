n1 = float(input("digite primeira nota:"))
n2 = float(input("digite segunda nota:"))
n3 = float(input("digite terceira nota:"))

n_media = round((n1 + n2 + n3) / 3, 1)

print(n_media)

if (n_media >= 5):
	print("Aprovado")
	
else:
	print("Reprovado")
	