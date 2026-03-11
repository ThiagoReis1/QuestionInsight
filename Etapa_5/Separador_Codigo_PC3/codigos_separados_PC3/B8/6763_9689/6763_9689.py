tempo = float(input("tempo de permanencia: "))
if tempo < 2:
	total = (tempo*1.25 )
elif tempo == 2:
		total = (tempo*2.25)
elif tempo > 2:
		total = (tempo*3.25)
print(round(total,2))