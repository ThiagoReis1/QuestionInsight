altura_luna = 1.65
taxa_luna = 0.02
contador=0
altalgm=float(input())
txcrescimento=float(input())
anos= 0
while altalgm<=altura_luna:
	altalgm+=txcrescimento
	altura_luna+=taxa_luna
	anos+=1
print(anos)
	