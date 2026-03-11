prc = float(input("Preco:"))
cdg = float(input("Codigo(1-4):"))
if(cdg == 1):
	vnd = prc - (prc*(40/100)) + prc*(10/100)
elif(cdg == 2):
	vnd = prc - (prc*(40/100)) + prc*(8/100)
elif(cdg == 3):
	vnd = prc - (prc*(40/100)) + prc*(0/100)
elif(cdg == 4):
	vnd = prc - (prc*(40/100)) + prc*(2/100)
print(round(vnd,2))