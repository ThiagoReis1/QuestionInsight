# faça seu código aqui!
s = input()

cnt = 0
i = 0
while i < len(s):
	if s[i].upper() == 'C':
		cnt += 1
	i += 1

print(cnt)