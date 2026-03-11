#Universidade federal do Amazonas
#Engenharia de producao
#Inroducao a Ciencia dos compuadores
#Allan Bezerra - 21552438

n = float(input("Digite o numero: "))

x = (n//1000)
y = (n%1000)
c = ((x-y))

if (c == n):
	print("X atende a propriedade")
else:
	print(int(c))