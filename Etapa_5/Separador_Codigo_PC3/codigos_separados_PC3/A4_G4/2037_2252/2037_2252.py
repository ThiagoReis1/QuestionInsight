id = int(input("idade:"))
p = 0
while (id != -1):
	if(id < 18):
		p = p + 1
	id = int(input("idade:"))
print(p)

