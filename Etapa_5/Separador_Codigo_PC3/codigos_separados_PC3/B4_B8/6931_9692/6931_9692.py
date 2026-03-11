vt = float(input("insira o valor total da compra: "))
c = input("insira o codigo: ")
if c == 'D':
	total = vt- (vt*0.18)
elif c == 'P':
	total = vt - (vt*0.18)
elif c == 'C':
	vezes = int(input("insira um numero: "))
	if vezes == 1:
		total = vt
	else:
		total = vt + (vt*0.07)
print (round(total,2))