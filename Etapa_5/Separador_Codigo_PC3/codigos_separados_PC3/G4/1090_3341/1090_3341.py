limi = float(input("limite:"))
var1 = float(input("valor1:"))
var2 = float(input("valor2:"))
var3 = float(input("valor3:"))
var4 = float(input("valor4:"))
var_total = var1 + var2 + var3 + var4
print(round(var_total, 2))
if (var_total <= limi):
   print("Dentro do limite")
else:
   print("Estorou o limite")
