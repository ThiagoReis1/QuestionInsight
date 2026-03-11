from numpy import*

hist = array(eval(input("")))


h = zeros(10, dtype=int)

acum = 0


for i in range(0, len(hist)-2):
	if hist[i] == hist[i+ 1] == hist[i + 2]:
		h[con] += 1
print(h)


