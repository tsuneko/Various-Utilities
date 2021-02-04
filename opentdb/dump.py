import urllib.request, json, html

print("getting token...")
token = ""
with urllib.request.urlopen("https://opentdb.com/api_token.php?command=request") as url:
    token = json.loads(url.read().decode())["token"]
print("done")

print("getting questions...")
dump = set()
a = 50
while True:
    with urllib.request.urlopen("https://opentdb.com/api.php?amount=" + str(a) + "&token=" + token) as url:
        data = json.loads(url.read().decode())
        if int(data["response_code"]) != 0:
            if a == 1:
                break
            else:
                a = a//2
        for i in range(len(data["results"])):
            dump.add(html.unescape(data["results"][i]["question"] + ": " + data["results"][i]["correct_answer"]))
print("done")
        
print("writing to disk...")
f = open("dump.txt","w",encoding="utf8")
for q in dump:
    f.write(q+"\n")
f.close()
print("done")
