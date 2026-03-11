r = float(input("Quantidade de ramem: "))
m = float(input("Quantidade de menma: "))
a = float(input("Quantidade de arroz: "))
o = float(input("Quantidade de onigi: "))

var1=7
var2=6
var3=3
var4=5

consumo=(var1*r)+(var2*m)+(var3*a)+(var4*o)
print(consumo)

a=consumo-3
b=consumo-consumo*0.10

if(consumo<=42):
	print(a, "ryous")
else:
	print(b, "ryous")
