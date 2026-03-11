rpm = int(input())
c = 0

while(rpm >= 40):
	rpm = rpm - (rpm * 2/100)
	c = c + 1
print(c)

