#Universidade Federal do Amazonas
#Icomp
#Larissa Magno Leão-21551610
#Exercicio 1

z=int(input("Informe qtd de zumbis Z:"))
h=int(input("Informe a qtd de habitantes H:"))
x=int(input("Informe a capacidade de transformar p em z por dia:"))
y=int(input("Informe a capacidade de matar zumbis por dia:"))

i=1

while(h>=z):
	
	z=z*x
	z=z-y
	h=h-x
	i=i+1
	
print(i)