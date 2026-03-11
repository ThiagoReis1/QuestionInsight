ca = 0.37
vf = 15.0
va = float(input("valor do volume de agua"))
vp = va*ca + vf
icm = 35/100 *vp
vt = vp + icm
print(round(vt,2))
