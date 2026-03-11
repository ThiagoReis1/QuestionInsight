s = input("nucleotideo: ").upper()
q = 0 # quant A
f = ""
while(s != "S"):
	f = f + s
	s = input("nucleotideo: ").upper()
	print(q)
	if(s == "A"):
		q = q + 1
		print(q)