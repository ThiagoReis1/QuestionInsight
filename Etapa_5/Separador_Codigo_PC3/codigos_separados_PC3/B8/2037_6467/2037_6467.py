idade = int(input())
a = 0
while True:
	if idade<18:
		a+=1
	elif idade == -1:
		break
print(a)