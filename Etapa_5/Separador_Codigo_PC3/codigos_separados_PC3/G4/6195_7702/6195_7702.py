b = int(input("n bacterias: "))
i = int(input("taxa de crescimento: "))
h = 0
tb = b

while tb < b*2:
	tb = ((i/100)*tb)+ tb
	h = h + 1
print(h)
