qi = int(input("quantidade inicial de moedas: "))
qf = int(input("despesa mensal: "))
qm= int(input("quantidade M: "))
qr = int(input("quantidade R: "))

qt = qi
m = 0

while(qt > 0):
	qt = qt - qf + qm - qr
	m = m + 1
print(m)