tempo = float(input())
a = 5000 + (100 * tempo)
c = tempo - 200
b = 8000 + (100 * 200) + (90 * c)
if(tempo <= 200):
	print(round(a,2))
else:
	print(round(b,2))