from numpy import*

speed = array(input().split(","))
race = zeros(5,dtype = int)

for i in range(size(speed)):
	if(speed[i] == "B"):
		race[0] = race[0] + 1
	if(speed[i] == "PA"):
		race[1] = race[1] + 1
	if(speed[i] == "PR"):
		race[2] = race[2] + 1
	if(speed[i] == "A"):
		race[3] = race[3] + 1
	if(speed[i] == "I"):
		race[4] = race[4] + 1
print(max(race))
print(race)