waifulistFile = open("waifulist.txt","r", encoding="utf-8")
mmsFile = open("mms_output.txt", "r", encoding="utf-8")
ownedlistFile = open("ownedlist.txt", "w", encoding="utf-8")

waifulist = []
for line in waifulistFile.readlines():
    l = line.rstrip()
    if '-' in l:
        l = l.split(' - ')[0]
    waifulist.append(l)

for line in mmsFile.readlines():
    l = line.rstrip()
    if ' | ' in l:
        l = l.split(' | ')[0]
    if l in waifulist:
        ownedlistFile.write(l+"\n")

ownedlistFile.close()
mmsFile.close()
waifulistFile.close()
