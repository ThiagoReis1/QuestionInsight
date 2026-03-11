userInp = int(input())

i = 0
k = 0

while (userInp != 0):
	i += 1
	if(userInp % 2 ==0):
		k += 1
	userInp = int(input())

prob = (k/i) * 100

print(i)
print(round(prob, 2))