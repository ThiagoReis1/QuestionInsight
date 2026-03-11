from numpy import *

s = input("digite a secao: ").upper()

Vf = 0
i = 0

while i < len(s):
	if s[i] == "H":
		Vf = Vf + 3.85
	elif s[i] == "L":
		Vf = Vf + 2.95
	elif s[i] == "E":
		Vf = Vf + 7.90 
	
	i = i + 1

print(round(Vf,2))