a = float(input("Peso da mercadoria a ser transportada:"))

var1 = float(a * 43.21)
var2 = int(25)
var3 = float(0.62*(var1+var2))
total = float(var1+var2+var3)

print(round(total, 2))