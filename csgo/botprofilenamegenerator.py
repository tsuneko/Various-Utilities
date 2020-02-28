import random

w = open("names.txt", "r")
names = []
for line in w.readlines():
	names.append(line.rstrip())
w.close()

c = 1

x = open("botprofile_names.db", "w")
for line in open("botprofile_base.db", "r").readlines():
	x.write(line)

diff = ["Expert", "Hard", "Normal", "Easy"]
diffI = 0
for i in range(len(names)):
    if i > 0 and diffI < 3 and i%(len(names)//4)==0:
        print("---")
        diffI += 1
    if i > 0 and i%((len(names)//4)//2)==0:
    	weapon = "Sniper"
    else:
    	weapon = "Rifle"
    x.write(diff[diffI] + "+" + weapon + " " + names[i] + "\n")
    print("Creating bot: " + names[i] + " (Difficulty: " + diff[diffI] + ", Weapon: " + weapon + ")")
    x.write("	VoicePitch = " + str(random.randrange(90,110)) + "\n")
    x.write("End\n\n")

x.close()

print("---\nDone.")
