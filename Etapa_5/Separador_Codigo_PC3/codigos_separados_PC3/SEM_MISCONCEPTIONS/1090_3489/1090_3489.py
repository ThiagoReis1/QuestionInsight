limite = float(input("digite o limite: "))
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
d = float(input("digite o valor de d: "))

valor = a + b + c+ d

if (valor <= limite) :
	frase = "Dentro do limite"
else:
	frase = "Estourou o limite"
	
print(round(valor,2))
print(frase)