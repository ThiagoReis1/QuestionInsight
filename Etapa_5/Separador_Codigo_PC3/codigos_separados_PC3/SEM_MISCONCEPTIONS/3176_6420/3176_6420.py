l = input(":")

vogal = 'aeiou'
consoante = 'bcdfghjklmnpqrstvwxyz'
v = 0
c = 0

for i in l:
	if i in vogal:
		v += 1
print(v)
for j in l:
	if j in consoante:
		c += 1
print(c)