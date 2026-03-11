from math import*

var1 = float(input("Alunos por m2: "))
var2 = float(input("Base maior: "))
var3 = float(input("Base menor: "))
var4 = float(input("Altura: "))

AT = var4*(var2+var3)/2

print(int(var1*AT))
