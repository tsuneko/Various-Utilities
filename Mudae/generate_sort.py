waifulistFile = open("waifulist.txt", "r", encoding="utf-8")
mmsFile = open("mms_output.txt", "r", encoding="utf-8")
sortFile = open("sort_command.txt", "w")

waifulist = []
for line in waifulistFile.readlines():
    l = line.rstrip()
    if '-' in l:
        l = l.split(' - ')[0]
    waifulist.append(l)

sortFile.write("$sm note ")
output = []
for line in mmsFile.readlines():
    l = line.rstrip()
    if ' | ' in l:
        l = l.split(' | ')[0]
    if l in waifulist:
        output.append(waifulist.index(l))
sortFile.write("$".join(list(map(lambda x: "Rank " + str(x+1), sorted(output)))))
sortFile.close()
mmsFile.close()
waifulistFile.close()
