from numpy import*

crs = input("Digite as cores: ").upper().split(',')
qts = zeros(5, dtype = int)

i = 0

while i < size(crs):
	if crs[i] == "P":
		qts[0] = qts[0] + 1
	elif crs[i] == "C":
		qts[1] = qts[1] + 1
	elif crs[i] == "M":
		qts[2] = qts[2] + 1
	elif crs[i] == "V":
		qts[3] = qts[3] + 1
	elif crs[i] == "A":
		qts[4] = qts[4] + 1

	i = i + 1

# Cor mais frequente
print(max(qts))
# Quantidades de cada cor
print(qts)