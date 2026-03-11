tempo = float(input("Tempo de voo: "))

if (tempo >= 0 and tempo <= 100):
	msg = tempo * 80 + 3000
elif (tempo >= 100 and tempo <= 200):
	msg = tempo * 90 + 4000
elif (tempo >= 200 and tempo <= 300):
	msg = tempo * 100 + 5000
else:
	msg = tempo * 110 + 6000
	
print(round(msg, 2))