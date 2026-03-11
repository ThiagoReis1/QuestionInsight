x = float(input())
k = int(input())

div = 1
count = 0

arctg = 0.0

while(count < k):
	arctg += (x ** div)/div
	div += 2
	count += 1

print(round(arctg, 7))