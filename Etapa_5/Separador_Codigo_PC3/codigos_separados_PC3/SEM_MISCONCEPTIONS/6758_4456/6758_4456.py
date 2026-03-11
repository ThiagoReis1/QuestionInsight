dias = int(input())

if dias < 7:
	total = dias * 100 + 15
elif dias == 7:
	total = dias * 100 + 12
else:
	total = dias* 100 + 10
	
print(round(total,2))
