from numpy import *
n =  array(eval(input("n: ")))
p = [4,3]
i = 0
pt = 0
nt = 0
pt = p[0] + p[1]
np0 = p[0] * n[0]
np1 = p[1] * n[1]
soma = np1 + np0
print(round((soma/pt),2))
	