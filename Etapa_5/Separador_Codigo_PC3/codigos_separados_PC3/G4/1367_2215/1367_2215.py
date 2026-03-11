qs = float(input("digite um numero:"))
qf = float(input("digite um numero:"))
qa = float(input("digite um numero:"))

qss = qs / 0.31
qff = qf / 0.73 
qaa = qa / 2.64

g = min(qss,qff,qaa)

print(int(g))
