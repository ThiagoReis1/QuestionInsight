from numpy import *

a = input("produtos: ").upper()

quant = 0
##
i = 0
while i < size(a):
	if a[i] == "H":
		quant = quant * 3.85
	if a[i] == "L":
		quant = quant * 2.95
	if a[i] == "E":
		quant = quant * 7.90
	i = i + 1

	
	
