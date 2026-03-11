s = input("").upper()
stg = ""
n = s.split(" ")
i = 0

while(i < len(n)):
	stg = stg + n[i][0]
	i = i + 1
print(stg)