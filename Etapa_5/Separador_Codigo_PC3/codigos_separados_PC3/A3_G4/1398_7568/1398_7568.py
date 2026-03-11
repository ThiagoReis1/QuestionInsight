t =  int(float(input("tempo: ")))
Vt = 5000.00+100.00*t
if (t <= 200):
	print(round(Vt,2))
else:
	Vt = 8000.00+100.00*(200) +90.00*(t-200)
	print(round(Vt,2))