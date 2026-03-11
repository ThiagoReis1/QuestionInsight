qc = float(input("combustivel comum "))
if qc < 17.5:
	d = qc + 10.5
elif qc > 17.5 and qc < 35.0:
	d = qc + 14
elif qc > 35 and qc < 50:
	d = qc + 18.6
elif qc == 50 or qc > 50:
	d = qc + 24.5
print(round(d,1))