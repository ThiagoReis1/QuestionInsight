from numpy import *
entr_nac = input().upper().split(",")
cont_nac = zeros(5, dtype = int)
nacio = "AR BR CL CO UY".split()

for entr in entr_nac:
	cont_nac[nacio.index(entr)] += 1

print(max(cont_nac))
print(cont_nac)