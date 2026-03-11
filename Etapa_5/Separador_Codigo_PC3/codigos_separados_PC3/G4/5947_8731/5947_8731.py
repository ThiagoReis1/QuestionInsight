a = input("C: ")
b = int(input("quantidade de c: "))
d = int(input("quantidade de sucos: "))
if a.lower() == "c":
	e = b*2 + d*6
	print(round(e,2))
else:
	f = b*4.5 +d*6		
	print(round(f,2))