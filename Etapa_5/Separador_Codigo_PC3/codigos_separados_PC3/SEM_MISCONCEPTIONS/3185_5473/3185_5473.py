inv = ""
frase = input("digite o algoritmo: ")

for palavra in frase.split(" "):
	inv += palavra[::-1]+""
	
print(format(inv))