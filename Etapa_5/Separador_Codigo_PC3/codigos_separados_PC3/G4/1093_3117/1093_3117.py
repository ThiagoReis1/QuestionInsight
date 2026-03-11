num = int(input("numero: "))

pri = num // 100
sec = num % 100

if pri**2 + sec**2 == num:
	msg = "atende"
else:
	msg = "nao atende"
print(msg)
print(num)