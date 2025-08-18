from numpy import*
pin = array(eval(input("")))
pin_novo = zeros(size(pin), dtype = int)
for i in range (size(pin)):
	if pin[i]== 0:
		pin_novo [i] = 9
	else:
		pin_novo[i] = pin[i]- 1
print(pin_novo)