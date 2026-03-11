aminoacido = input()
O=15.9994
C=12.011
N=14.00674
H=1.0079

histidina = ((6 * 12.011) + (10 * 1.0079) + (3 * 14.00674) + (2 * 15.9994))
leucina = ((6 * 12.011) + (13 * 1.0079) + (14.00674) + (2 * 15.9994))
lisina = ((6 * 12.011) + (15 * 1.0079) + (2 * 14.00674) + (2 * 15.9994))
if(aminoacido =="Histidina".lower):
	print(round(histidina,2))
if(aminoacido == "Leucina".lower):
	print(round(leucina,2))
if(aminoacido == "Lisina".lower):
	print(round(lisina,2))