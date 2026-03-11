rpm = float(input('type a begin rotation: '))
seconds = 0

while(rpm>=40):
	rpm = rpm - (rpm*0.02)
	seconds = seconds+1
	
print(seconds)
