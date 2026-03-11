from numpy import *

liq = input("produtos: ").upper

A = 16.75
L = 4.60
P = 2.85

i = 0

if (("A" in liq) and ("L" in liq) and ("P" in liq)):
	soma = liq + A + L + P
	print(round(soma, 2))
	