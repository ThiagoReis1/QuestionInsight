# 0 - AZ - Arizona
# 1 - CA - Califórnia
# 2 - FL - Flórida
# 3 - PA - Pensilvânia
# 4 - WI - Wisconsin

import numpy as np

entrada = input("Informe os dados: ").split(",")

conta = np.zeros(5, dtype = int)

for i in entrada:
	if (i.upper() == "AZ"):
		conta[0] += 1
	elif (i.upper() == "CA"):
		conta[1] += 1
	elif (i.upper() == "FL"):
		conta[2] += 1
	elif (i.upper() == "PA"):
		conta[3] += 1
	elif (i.upper() == "WI"):
		conta[4] += 1
		
print(max(conta))
print(conta)


