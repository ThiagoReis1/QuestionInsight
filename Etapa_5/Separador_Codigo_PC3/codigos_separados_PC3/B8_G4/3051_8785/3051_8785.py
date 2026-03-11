val= float(input(':'))

if val >= 0. and val <= 150.:
	nv = val * 0.6 + 5.
elif val > 150. and val <= 250.:
	nv = val * 0.65 + 8.
elif val > 250. and val <= 350.:
	nv = val * 0.7 + 12.
elif val > 350.:
	nv = val * 0.75 + 16.

print(round(nv,2))