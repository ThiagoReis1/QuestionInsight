m = int(input(""))

anos = 0

while(m >= 0.5):
	total = m * 0.10
	m = m - total
	anos = anos + 1
print(anos)
