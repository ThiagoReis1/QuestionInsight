var1 = float(input("quantos gramas possui seu prato:"))
var2 = int(input("quantidade de bebidas:"))
var3 = int(input("quantidade de sobremesas:"))
x = (var1/1000)
a = 26.90
b = 3.50
c = 3.00
valor=(x*a+var2*b+var3*c)
print(round(valor, 2 ))