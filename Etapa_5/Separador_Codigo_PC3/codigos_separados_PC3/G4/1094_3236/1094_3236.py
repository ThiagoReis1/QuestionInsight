a = int(input())

n1 = a // 100000
n1r = a % 100000
n2 = n1r // 10000
n2r = n1r % 10000
n3 = n2r // 1000
n3r = n2r % 1000
n4 = n3r // 100
n4r = n3r % 100
n5 = n4r // 10
n5r = n4r % 10
n6 = n5r // 1


f = (((n1 * 100 + n2 * 10) + n3) + ((n4 * 100 + n5 * 10 + n6))) ** 2

if (f == a):
	print("atende")
else:
	print("nao atende")
print(a)