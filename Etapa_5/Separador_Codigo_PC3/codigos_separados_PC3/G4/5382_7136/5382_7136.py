from numpy import* 

v = input(": ").upper()
i = 0
vo = 0
o = 0

while i < len(v):
	if v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U":
		vo = vo + 0.25
	else:
		o = o + 0.27
	i = i + 1

t = vo + o

print(round(t, 2))


		
		
		
		
	

