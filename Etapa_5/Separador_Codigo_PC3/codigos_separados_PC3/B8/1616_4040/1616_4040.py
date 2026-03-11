from numpy import *

# Notes to myself:

# The table in the left indicates the damage of a sorcerie by level of the caster, ergo I can define the sorcerie by it's damage per level

# Entries

sorcery = array(eval(input("Insert type of sorcery: ")))
level = array(eval(input("Insert level of mage: ")))

# Definitions

i = 0
s = size(level)
dpl = zeros(s)
dmg = 0

# Processing

while(i < s):
	if(sorcery[i] == ("GELO")):
		dpl[i] += 2
	elif(sorcery[i] == ("FOGO")):
		dpl[i] += 3
	elif(sorcery[i] == ("CHOQUE")):
		dpl[i] += 4
	elif(sorcery[i] == ("CONJURACAO")):
		dpl[i] += 8
	elif(sorcery[i] == ("ILUSAO")):
		dpl[i] += 10
	dmg = dmg + (dpl[i])*(level[i])
	i += 1
	
print(dmg)	