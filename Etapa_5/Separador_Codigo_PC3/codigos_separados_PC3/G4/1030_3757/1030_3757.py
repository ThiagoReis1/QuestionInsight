bb=45
mix=0.97
icms=0.42
qm=float(input("minutos exd"))
vt=bb+(mix*qm)
v= vt+vt*icms
print(round(v, 2))