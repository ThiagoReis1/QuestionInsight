quant = int(input("pontos de vida restante: "))
s1 = int(input("s1: "))
s2 = int(input("s2: "))
s3 = int(input("s3: "))

soma = 10*(s1+s2+s3)

if(soma >= 0):
	print(soma)
	print("VIVO")
else:
	print(soma)
	print("MORTO")
