from numpy import*
entry = input("Estado: ").split(',')
estados = ["AZ","CA","FL","PA","WI"]
result = zeros(5,dtype=int)

for i in entry:
	if i == "AZ":
		result[0] = result[0] + 1
	if i == "CA":
		result[1] = result[1] + 1
	if i == "FL":
		result[2] = result[2] + 1
	if i == "PA":
		result[3] = result[3] + 1
	if i == "WI":
		result[4] = result[4] + 1

print(max(result))
print(result)