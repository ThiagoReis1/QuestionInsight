
v = float(input(""))
m = float(input(""))
j = float(input(""))

s = v
tempo = 0 

if(v > 0 and m > 0 and j > 0):
	while(s < v + (v * 20 / 100)):
		s = (round((s + (s * j)/100)-m, 2))
		tempo = tempo + 1
	print(tempo)
else:
   print("Dados incorretos")
