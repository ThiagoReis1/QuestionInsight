cont = 0
con = 0
n = int(input())
while n != -1:
	cont += 1
	if n >= 45 and n <= 150:
		con += 1
	n = int(input())
print(con)