from numpy import *

s = input("Digite a string: ").upper()
i = 0
acumi = 0
acumm = 0
acums = 0
total = 0 
while i < len(s):
	if s[i] == "I":
		total = total+3.75
		acumi = acumi + 1 
	elif s[i] == "M":
		total = total+ 4.50 
		acumm = acumm + 1
	elif s[i] == "S":
		total = total+2.90
		acums = acums + 1
	i +=1
print(round(total,2),acumi,acumm,acums)
