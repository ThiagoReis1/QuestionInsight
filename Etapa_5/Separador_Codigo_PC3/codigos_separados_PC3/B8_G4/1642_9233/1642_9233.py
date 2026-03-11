
v = array(eval(input("quantidade de cinco alunos: ")))

cinco = 0 
 #contar grupos
for i in range(size(v)):
	if (v[i]%5 ==0):
		cinco+= 1
		
#vetor com quantidade de cinco 
a = zeros(cinco, dtype = int)

x=0
for i in range(size(v)):
	if i == 0 and v [0] % 5 ==0:
		a[0] = 0 
		x+=1
	elif(v[i] % 5 ==0):
		a[x]= i
		x += 1
print(cinco)
print(a)
