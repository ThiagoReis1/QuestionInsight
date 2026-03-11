dias = int(input(""))

if dias < 15:
	total = (175 * dias) + 20
elif dias == 15:
	total = (175 * 15) + 16
elif dias > 15:
	total = (175 * dias) + 10
	
print(round(total,2))







