s = input("Satisfacao: ")
sim = 0

while(s.upper() != "S"):
	if (s.upper() == "SIM"):
		sim = sim + 1
		s = input("Satisfacao: ")
	else:
		s = input("Satisfacao: ")
print(sim)