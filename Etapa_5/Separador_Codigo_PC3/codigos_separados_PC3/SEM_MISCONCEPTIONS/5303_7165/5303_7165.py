decresc = 0.1
massa = float(input("Massa incial: "))
anos = 0
while(massa > 0.5):
	massa = massa - massa*decresc
	anos = anos + 1
print(anos)
	
	