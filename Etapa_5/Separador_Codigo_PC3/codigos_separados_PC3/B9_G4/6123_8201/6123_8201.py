qc=float(input())
if qc<17.5:
	e=qc+0.8
	print(e)
elif qc>=17.5 and qc<35:
	e=qc+1.3
	print(e)
elif qc>35 and qc<50:
	e=qc+2.1
	print(e)
else:
	e=qc+3
	print(e)