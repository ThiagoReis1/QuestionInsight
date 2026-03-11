from numpy import *

gols = input().upper()

gols = gols.split(",")

gols_jog = zeros(4,dtype=int)

for i in gols:
	if i == 'A':
		gols_jog[0] += 1
	if i == 'B':
		gols_jog[1] += 1
	if i == 'C':
		gols_jog[2] += 1
	elif i == 'D':
		gols_jog[3] += 1

print(gols_jog)