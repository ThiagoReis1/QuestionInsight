from numpy import *
n = input("").upper()
o = 0
if "P" not in n:
	print("nao achei")
else:
	while o < len(n):
		if n[o]=="P":
			print(o)
		o+=1
	