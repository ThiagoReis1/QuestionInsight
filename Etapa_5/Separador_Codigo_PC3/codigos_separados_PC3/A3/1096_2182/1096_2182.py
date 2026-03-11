num = int(input(":"))
a = num // 100000
rst_a = num % 100000

b = rst_a // 10000
rst_b = rst_a % 1000

c = rst_b // 1000
rst_c = rst_b % 1000

d = rst_c // 100
rst_d = rst_c % 100

e = rst_d // 10
rst_e = rst_d % 10

f = rst_d 

x = a + b + c
y = d + e + c

if(num == (x - y)**3 ):
	msg = "atende"
	print(num)

else:
	msg = " nao atende "
	print(num)

print(msg)
 
