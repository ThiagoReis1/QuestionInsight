p = float(input("peso em gramas: "))
qd = float(input("quantidade em gramas: "))
d = (p-qd)*7
R = d/p
s = (d%p)
print(round(s,4))