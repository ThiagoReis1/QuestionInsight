cons = float(input("consumo:"))

icms = (31 / 100)

vt = (0.28 * cons) + 23

vt2 = (vt * icms)

vt3 = ( vt + vt2 )
print (round(vt3,2))