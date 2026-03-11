from numpy import*
nota = array(eval(input(" ")))
i = 0
j = 0
t = 0
rep = 0
r = zeros(2, dtype=int)
for i in range(size(nota)):
	if nota[i] > 5:
		t = t + 1
		#print(t)
		
for j in range(size(nota)):
	if nota[j] < 5:
		rep = rep + 1
		#print(resultado)
		
   #r = zeros(2, dtype=int)
r[0] = t
r[1]= rep
print(t)
print(r)
