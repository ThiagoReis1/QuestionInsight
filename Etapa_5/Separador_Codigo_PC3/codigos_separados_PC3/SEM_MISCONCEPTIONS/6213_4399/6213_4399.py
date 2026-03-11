num = int(input())
quant_num = 0
while num >= 0:
	if num >= 101 and num <= 201:
		quant_num += 1
	num = int(input())
print(quant_num)