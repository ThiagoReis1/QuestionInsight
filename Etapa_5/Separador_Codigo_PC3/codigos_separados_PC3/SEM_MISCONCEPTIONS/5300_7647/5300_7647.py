rpm = float(input("Insira o RPM: "))

while(rpm > 50):
	velrotf = rpm
	print(round(velrotf, 2))
	rpm = rpm - rpm * 0.25