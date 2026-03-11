from math import*
var1 = float(input("valor inicial: "))
var2 = float(input("valor final: "))
var3 = int(input("num de anos: "))

#taxa de juros var4
var4 = (log(var2) - log(var1))/var3

print(var4)