a = int(input("quantidade de votos: "))
d = int(input("quantidade de votos: "))
n1 = a+d
calca = (a/n1)*100
calcd = (d/n1)*100


if(a>d):
	print("Ambrosio Rutra")
	print(round(calca, 2))
else:
	print("Demelza Olecram")
	print(round(calcd, 2))



