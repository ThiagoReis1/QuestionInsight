from numpy import*
vet = array(eval(input("vetor")))
t = 0
for i in vet:
	if i%5 == 0:
		n = 1
vet2 = zeros(n, dtype = int)
t += 1
n += 1
p = 0
p1 = 0
for e in vet:
   if i%5 == 0:
      vet2[p1] = p
      p1 += 1
   p += 1
print(t)
print(vet2)