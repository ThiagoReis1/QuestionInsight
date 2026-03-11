num=int(input())
n1= num // 10000
resto_r1= num % 10000
s = (n1 + resto_r1)**2
print(num)
if s == num:
	print("atende")
else:
   print("nao atende")

