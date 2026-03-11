comb = float(input())
dose = 0

if comb < 17.5:
	dose = 10.5
elif comb < 35:
	dose = 14
elif comb < 50:
	dose = 18.6
else:
	dose = 24.5

total = comb + dose
print(round(total,1))