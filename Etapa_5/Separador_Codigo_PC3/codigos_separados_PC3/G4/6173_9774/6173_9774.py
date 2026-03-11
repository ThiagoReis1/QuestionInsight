res = input("Atendimento satisfatorio?: ").upper()

ssim = 0

while (res != "S"):
	if (res == "SIM"):
		ssim += 1
	res = input("Atendimento satisfatorio?: ")
	
print(ssim)