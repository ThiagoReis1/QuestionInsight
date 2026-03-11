gen = input("qual o genero: ").upper()
sub = input("subgenero: ").upper()

if(gen == "INVESTIGATIVA") and (sub == "SUSPENSE"):
	ser = "DEXTER"
	print(ser)
elif(gen == "INVESTIGATIVA") and (sub == "DRAMA"):
	ser = "NARCOS"
	print(ser)
elif(gen == "DRAMATICA") and (sub == "COM FICCAO"):
	ser = "LOST"
	print(ser)
elif(gen == "DRAMATICA") and (sub == "AVENTURA"):
	ser = "SHERLOCK"
	print(ser)
else:
	print("SERIE NAO IDENTIFICADA")
	