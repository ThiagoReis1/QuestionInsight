altm = 1.86
taxm = 0.01
altc=float(input("altc: "))
taxc=float(input("tax: "))
a = 0

while altc < altm:
	altm = altm + taxm
	altc = altc + taxc
	a = a + 1 

print(a)	