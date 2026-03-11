resp = input("O cliente esta satifeito? SIM ou NAO: " ).upper()

cont = 0

while resp != "S":
	if resp == "SIM":
		cont += 1
	resp = input("Outro cliente esta satisfeito? Sim (S) ou Nao (N) ").upper()

print(cont)
	
