alturacicero = 1.8
taxacicero = 0.01
ac = float(input("altura"))
tc = float (input("taxa de crescimento"))
a = 0
while alturacicero > ac:
	ac = ac+tc
	alturacicero = alturacicero + taxacicero
	a +=1
print(a)