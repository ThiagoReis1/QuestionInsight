minutos = float(input("digite um numero:"))
p = (0.28 * minutos)
vm = 23
vt= p + vm
icms= vt*(31/100)
var = vt + icms
print(round(var, 2))