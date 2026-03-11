# faça seu código aqui!
from numpy import*
s = input("digite string: ").upper()
l = "N"

i = 0

while i < len(s):
	if s[i]=="N":
	   print(i)
	i = i +1
if "N" not in s:
	print("nao achei")
	
	
	