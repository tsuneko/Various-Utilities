import urllib.request, json, html

n = 0

dump = set()
f = open("opentdb_dump.txt", "r", encoding="utf8")
for l in f.readlines():
    dump.add(l.rstrip())
    n += 1
f.close()

try:
    while True:
        with urllib.request.urlopen("https://opentdb.com/api.php?amount=100") as url:
            data = json.loads(url.read().decode())
            for i in range(len(data["results"])):
                s = data["results"][i]["question"] + ": " + data["results"][i]["correct_answer"]
                s = html.unescape(s)
                if s not in dump:
                    dump.add(s)
                    n += 1
                    print(n)
except:
    pass

print("writing to file...")
f = open("opentdb_dump.txt","w", encoding="utf8")
for q in dump:
    f.write(q+"\n")
f.close()
print("done")
