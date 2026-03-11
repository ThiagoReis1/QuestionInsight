tempo = int(input("tempo: "))
if (tempo <= 100):
	print(tempo * 80 + 3000)
elif(tempo > 100 and tempo <= 200):
	print(tempo * 90 + 4000)
elif(tempo > 200 and tempo <= 300):
	print(tempo * 100 + 5000)
else:
	print(tempo * 110 + 6000)