num = int(input())
dig1_2 = num // 100
rest1_2 = num % 100
dig3_4 = rest1_2 // 1
if((dig1_2)**2 +(dig3_4)**2 == num):
	print("atende")
else:
	print("nao atende")
print(num)