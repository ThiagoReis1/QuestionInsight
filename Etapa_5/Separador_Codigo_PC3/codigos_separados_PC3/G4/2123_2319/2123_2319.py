from numpy import*
x = array(eval(input()))
i = 0 
t = []
while i < size(x):
	if x[i] > min(x):
		t.append(x[i])
	i+=1
Mfinal = (sum(t)/3)
print(round(Mfinal,2))
if Mfinal > 5 :
	print("APROVOU")
else:
	print("REPROVOU")