num = int(input("Numero: "))
part1 = (num // 100)
part2 = (num % 100)
x = ((part1 ** 2) + (part2 ** 2))

if( num == x):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)