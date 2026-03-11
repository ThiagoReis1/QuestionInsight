from math import *
n_p = float(input())
qs = float(n_p * ((sqrt(5) - 1) / 4) )
qsa = float(n_p * sqrt(5 - 2 * sqrt(5)) )
qa = float(n_p * 5 * ( 5 - 2* sqrt(5)) )

print(round(qs, 2))
print(round(qsa, 2))
print(round(qa, 2))