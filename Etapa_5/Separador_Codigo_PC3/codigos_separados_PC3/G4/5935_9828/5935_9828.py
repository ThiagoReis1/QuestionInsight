p = float(input("Informe o peso da mercadoria que sera transportada: "))
vp = (p*43.21)+25
vt = vp+(31/50*vp)

print(round(vt,2))