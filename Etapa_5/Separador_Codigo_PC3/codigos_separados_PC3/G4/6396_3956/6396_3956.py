import numpy as np
inp = input()
inp = inp.replace("[", "").replace("]", "").replace(",", "")
new = []
for i in range(len(inp)):
	new.append(2*int(inp[i]))

new = np.array(new)
print(new)