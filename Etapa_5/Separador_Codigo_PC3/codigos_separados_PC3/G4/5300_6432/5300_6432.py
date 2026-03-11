vel = float(input(""))

while (vel > 50):
	print(round(vel,2))
	vel = vel - (vel * (25/100))
	#print(round(vel,2))