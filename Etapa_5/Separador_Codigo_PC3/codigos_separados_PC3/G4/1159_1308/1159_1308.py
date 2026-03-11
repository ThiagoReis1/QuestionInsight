no=float(input('qi tambaqui:'))
nop=float(input('qi de pacu:'))
txtmb=float(input('tx anual/ tambaqui entre 0 e 1:'))
txpc=float(input('tx anual de pacus entre 0 e 1:'))
numax=float(input('max de especies'))
i=1
p=0
while p<numax:     
    nat=no+no*txtmb
    natp=nop*txpc
    p=p+nat+natp
    i=i+1
print(i)
	

