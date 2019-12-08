f = open("waifulist.txt","r", encoding="utf-8")
w = open("waifulist_commands.txt", "w", encoding="utf-8")
waifus = []
for line in f.readlines():
    l = line.rstrip()
    li = 0
    if '-' in l:
        l = l.split(' - ')[0]
    if l == "":
        break
    waifus.append(l)


for i in range(len(waifus)//5):
    w.write("$l ")
    for j in range(5):
        if j < 4:
            w.write(waifus[i*5+j] + "$")
        else:
            w.write(waifus[i*5+j] + "\n")

w.write("\n\n")

for i in range(len(waifus)):
    w.write("$note " + waifus[i] + "$Rank " + str(i+1) + "\n")

    
f.close()
w.close()
