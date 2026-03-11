valor1 = int(input("peso: "))
valor2 = int(input("distancia: "))

var1 = valor1 * 25
var2 = valor2 * 0.10
preco = var1 + var2
imposto = preco * 0.12
servico = preco + imposto
print(float(round(servico, 2)))