vel = float(input("velocidade inicial do peao: "))
rpm = vel
red = 0
while(rpm > 65):
	rpm  = rpm - red
	red = (25/100) * rpm
	print(round(rpm,2))