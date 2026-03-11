t = int(input("numero de tambaqui:"))
p = int(input("numero de pacus:"))
ct = int(input("taxa anual de crescimento de tambaqui:"))
cp = int(input("taxa anual de crescimento de pacu:"))
n = int(input("numero maximo de especies comportadas pelo viveiro:"))
a = 0

while (t+p) <= n:
	rt = t * (ct/100)
	rp = p * (cp/100)
	t = t + rt
	p = p + rp
	a = a + 1
	
print(a)