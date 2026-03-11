altura_luna = 1.65
taxa_luna = 0.02
l=float(input("altura "))
t=float(input("taxa de crescimento"))
anos=0
while l < altura_luna:
	altura_luna+=taxa_luna
	l+=t
	anos+=1
print(anos)
	