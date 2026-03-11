from numpy import *

estado = input("Estados: ").upper().split(",")
arizona = 0
california = 0
florida = 0
pensilvania = 0
wisco = 0

for x in estado:
	if x == "AZ":
		arizona = arizona + 1
	if x == "CA":
		california = california + 1
	if x == "FL":
		florida = florida + 1
	if x == "PA":
		pensilvania = pensilvania + 1
	if x == "WI":
		wisco = wisco + 1
		
ESTADO = zeros(5, dtype = int)
ESTADO[0] = arizona
ESTADO[1] = california
ESTADO[2] = florida
ESTADO[3] = pensilvania
ESTADO[4] = wisco
print(max(ESTADO))
print(ESTADO)