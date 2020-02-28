import random

w = open("names.txt", "r")
names = []
for line in w.readlines():
    names.append(line.rstrip())
    print(line.rstrip())
w.close()

c = 1

x = open("botprofile_names.db", "w")
for line in open("botprofile_base.db", "r").readlines():
    x.write(line)

botDifficulties = ["Expert", "Hard", "Normal", "Easy"]
botDifficultyIndex = 0
for i in range(len(names)):
    if botDifficultyIndex < 3 and i%(len(names)//4)==0:
        print(i)
        botDifficultyIndex += 1
    if i%(len(names)//8)==0:
        weapon = "Sniper"
    else:
        weapon = "Rifle"
    x.write(botDifficulties[botDifficultyIndex] + "+" + weapon + " " + names[i] + "\n")
    x.write("	VoicePitch = " + str(random.randrange(90,110)) + "\n")
    x.write("End\n\n")

x.close()
