q1 = float(input("quantidade de snowberry: "))
q2 = float(input(" quantidade de sais de fogo: "))
q3 = float(input("quantidade de amanita: "))

qm1 = q1/0.31
qm2 = q2/0.73
qm3 = q3/2.64

qmax = min(qm1, qm2, qm3)

print(int(qmax))