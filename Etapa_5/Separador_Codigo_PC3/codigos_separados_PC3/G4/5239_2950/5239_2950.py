n = float(input())

if(n >= 9 and n <= 10):
	nota = "A"
elif(n >= 8 and n < 9):
	nota = "B"
elif(n >= 7 and n < 8):
	nota = "C"
elif(n >= 6 and n < 7):
	nota = "D"
elif(n >= 4 and n < 6):
	nota = "E"
elif(n < 4 and n >= 0):
	nota = "F"
else:
	nota = "ERRO"
	
print(nota)