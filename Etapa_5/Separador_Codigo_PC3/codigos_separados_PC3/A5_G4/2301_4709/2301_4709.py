import match

var1 = float(input("O lado b:"))
var2 = float(input("O lado c:"))
var3 = float(input("O angulo alfa entre b e c (em graus):"))
a = float((var1**2) + (var2**2) - (2*var1*var2) * radians(var3))

print(round(a, 2))