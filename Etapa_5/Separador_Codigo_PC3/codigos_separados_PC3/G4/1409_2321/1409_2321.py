ata = input()

d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

a1 = 6 + d1
a2 = 6 + d2
a3 = 6 + d3
a4 = 6 + d4

at = a1 + a2 + a3 +a4

danc = (d1 + d2 +d3)*d4

if d1 <= 6 and d2 <= 6 and d3 <= 6 and d4 <= 6:
	
	if ata == "espada":
		print(at)
	if ata == "cauda":
		print(danc)
