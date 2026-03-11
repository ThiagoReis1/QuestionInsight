a = int(input())

n1 = a // 1000
n1r = a % 1000
n2 = n1r // 100
n2r = n1r % 100
n3 = n2r // 10
n3r = n2r % 10
n4 = n3r // 1

f = ((n1 * 10 + n2) + (n3 * 10 + n4)) ** 2
print(a)
if (f == a):
	print("atende")
else:
	print("nao atende")