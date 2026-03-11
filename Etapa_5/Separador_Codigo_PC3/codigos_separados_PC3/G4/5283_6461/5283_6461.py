num = int(input("digite o numero: "))

pos = 0
n = 0
while num != 0:
	if num > 0:
		pos = pos + 1
	else:
		n = n + 1
	num = int(input("digite o numero: "))
total_num = pos + n
pcr = (pos / total_num) * 100 

print(total_num)
print(round(pcr, 2))