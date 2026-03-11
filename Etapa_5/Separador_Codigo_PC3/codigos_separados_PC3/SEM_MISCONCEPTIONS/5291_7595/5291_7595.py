resposta = input("Reposta: ").upper()

total = 0
total_sim = 0

while(resposta != "S"):
	total = total + 1
	if(resposta == "SIM"):
		total_sim = total_sim + 1
	resposta = input("Resposta: ").upper()
if(resposta == "S"):
	print(total)
	print(round((total_sim/total)*100,2))
		