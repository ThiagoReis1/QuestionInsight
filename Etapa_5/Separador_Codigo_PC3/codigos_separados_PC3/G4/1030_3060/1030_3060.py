mex = float(input("Insira a quantidade de minutos: "))
g = 45 + (mex * 0.97)
icms = g * (42/100)
vt = g + icms

print(round(vt,2))