from numpy import zeros
final = zeros(5, dtype = int)
paises = input().split(',')
for pais in paises:
	if pais == "BE":
		final[0] += 1
	elif pais == "ES":
		final[1] += 1
	elif pais == "FR":
		final[2] += 1
	elif pais == "IT":
		final[3] += 1
	elif pais == "PT":
		final[4] += 1
print(max(final))
print(final)