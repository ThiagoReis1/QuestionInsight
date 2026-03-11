con = float(input(""))

if(con >= 0) and (con < 150):
	v = con * 0.60 + 5
elif(con >= 150) and (con < 250):
	v = con * 0.65 + 8
elif(con >= 250) and (con < 350):
	v = con * 0.70 + 12
elif(con >= 350):
	v = con * 0.75 + 16
print(round(v, 2))