import os

settings = {}
settings["en"] = True
settings["viewer"] = True

if os.path.isfile("review.txt"):
    f = open("review.txt", "r")
    for line in f.readlines():
        keys = [k for k in line.rstrip().split("=")]
        if len(keys) == 2:
            if keys[1].strip().lower() == "true":
                settings[keys[0]] = True
            else:
                settings[keys[0]] = False
    f.close()
else: 
    p = subprocess.Popen("set OMP_NUM_THREADS=8", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("review.txt", "w")
    f.write("en=true\nviewer=true")
    f.close()
    
url = input("Enter Tenhou/Mahjong Soul replay url= ").rstrip()
while url:
    cmd = "set OMP_NUM_THREADS=8&&cd akochan-reviewer&&akochan-reviewer.exe"
    if settings["en"]:
        cmd += " --lang en"
    if not settings["viewer"]:
        cmd += " --without-viewer"
    cmd += " " + url
    os.system(cmd)
    url = input("Enter Tenhou/Mahjong Soul replay url= ")
