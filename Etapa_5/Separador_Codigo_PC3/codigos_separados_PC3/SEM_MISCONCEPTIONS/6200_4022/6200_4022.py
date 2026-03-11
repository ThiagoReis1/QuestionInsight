altmax = 1.75
txmax = 0.01
alt = float(input())
tx = float(input())
cont = 0

while alt<altmax:
		altmax = altmax + txmax
		alt = alt + tx
		cont = cont + 1
print(cont)