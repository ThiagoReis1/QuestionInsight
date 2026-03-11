from numpy import*

p = array(eval(input("numero: ")))
i = 0
s = 100

while i < size(p):
	if p[i] == 1:
		s =  s*5
	elif p[i] == 2:
		s =  s*3
	elif p[i] == 3:
		s = s
	elif p[i] == 4:
		s =  s/2
	i = i + 1
print(round(s, 2))