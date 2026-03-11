q=float(input("combustivel"))
if q<17.5:
	v=q+1.5
	print(round(v,2))
if q>=17.5 and q<35:
	v=q+2.3
	print(round(v,2))
if q>=35 and q<50:
	v=q+3.3
	print(round(v,2))
if q>=50:
	v=q+4.7
	print(round(v,2))
