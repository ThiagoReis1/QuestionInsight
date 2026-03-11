alturacicero = 1.75
taxacicero = 0.01

alt = float(input("altura:"))
tx = float(input("taxa: "))
a = 0
while alturacicero > alt:
	alturacicero = alturacicero + taxacicero
	alt = alt+tx
	a += 1
print (a)