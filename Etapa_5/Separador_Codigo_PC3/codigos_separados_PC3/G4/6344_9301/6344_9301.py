from numpy import *
s = input("s: ")
if len(s) >= 5 and (s[4].lower() == "c"):
	print(s.upper())
else:
	print("nome invalido")
						  