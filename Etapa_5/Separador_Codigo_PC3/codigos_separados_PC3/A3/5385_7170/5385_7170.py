from numpy import *

a = str(input("Palavra: ").upper())

vogal = 0
cons = 0

while a in "AEIOU":
	print(sum(vogal in "AEIOU"))
	