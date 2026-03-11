vp= 9.80
tm= 20
icms= .15
pecas= float(input("quant de p de ped no cam: "))
sub= pecas*vp+tm
vt= sub + (sub*.15)
print(round(vt, 2))