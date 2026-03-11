v = float(input("insira o valor total da compra:"))
p = input('insira C ou P ou D:').upper()
des= v*(13/100)
d= v*(8/100)
if p == 'C':
	s=input("insira 1 ou 2:")
	if s =='1':
		t=v
	else:
		t=v+d
elif p=='P':
	t=v-des
else:
	t=v-des
print(round(t,2))
		
		