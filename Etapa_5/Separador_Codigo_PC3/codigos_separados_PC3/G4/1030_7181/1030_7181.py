pc=45
mex=0.97
icms=0.42
qm=float(input("entre com a quantidade de minutos excedente: "))
vt=pc+(mex*qm)
v= vt+vt*icms
print(round(v, 2))