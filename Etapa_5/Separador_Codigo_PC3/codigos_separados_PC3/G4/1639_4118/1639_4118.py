from numpy import*
t = array(eval(input("Aluno: ")))
p = 0

for i in range(size(t)):
	if(t[i]%2 == 0):
		p += 1
z = zeros(p, dtype = int)
i = 0
for ip in range(size(t)):
	if(t[ip]%2 == 0):
		z[i] = ip
		i += 1
print(p)
print(z)