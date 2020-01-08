waifulistFile = open("waifulist.txt","r", encoding="utf-8")
waifulist = []
for line in waifulistFile.readlines():
    l = line.rstrip()
    if '-' in l:
        l = l.split(' - ')[0]
    waifulist.append(l)
waifulistFile.close()

mmsFile = open("mms_output.txt", "r", encoding="utf-8")
ownedlistFile = open("ownedlist.txt", "w", encoding="utf-8")
ownedwaifulist = []
ownedwaifuranks = []
for line in mmsFile.readlines():
    l = line.rstrip()
    if ' | ' in l:
        l = l.split(' | ')[0]
    if l in waifulist:
        ownedlistFile.write(l+"\n")
        ownedwaifulist.append(l)
        ownedwaifuranks.append(waifulist.index(l))
ownedlistFile.close()
mmsFile.close()

commandsFile = open("commands.txt", "w", encoding="utf-8")

commandsFile.write("Like List\n")
for i in range(len(waifulist)//5):
    commandsFile.write("$l ")
    for j in range(5):
        if j < 4:
            commandsFile.write(waifulist[i*5+j] + "$")
        else:
            commandsFile.write(waifulist[i*5+j] + "\n")
commandsFile.write("\n\n")

commandsFile.write("Notes\n")
for i in range(len(waifulist)):
    if waifulist[i] in ownedwaifulist:
        commandsFile.write("$note " + waifulist[i] + "$Rank " + str(i+1) + "\n")
commandsFile.write("\n\n")

commandsFile.write("Sort\n")
commandsFile.write("$sm note " + "$".join(list(map(lambda x: "Rank " + str(x+1), ownedwaifuranks))))  
commandsFile.close()

print("Done.")
