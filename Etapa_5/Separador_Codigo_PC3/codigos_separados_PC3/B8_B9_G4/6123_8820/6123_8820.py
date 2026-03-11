qc = float(input("deh a qdd: "))
v1 = qc+0.8
v2 = qc+1.3
v3 = qc+2.1
v4 = qc+3
if qc<17.5:
	print (round(v1, 1))
elif qc>=17.5 and qc < 35:
	print(round(v2,1))
elif qc >= 35 and qc < 50:
	print(round(v3,1))
elif qc >= 50:
	print (round (v4,1))