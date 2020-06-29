#!/usr/bin/python3
import git
import os
import shutil
import time

repo_url = "https://github.com/Oduvancheg666/daisy.github.io.git" 

git.Git("./").clone(repo_url)
os.popen("cp ./daisy.github.io/script.js /opt/bot/phrases")
time.sleep(0.1)
shutil.rmtree("./daisy.github.io")

phrases = []
with open("/opt/bot/phrases", "r") as file:
    lines = file.readlines()
    for line in lines:
        if len(line.strip()) > 0:
            phrases.append(line.strip().replace('"', "")[:-1])


with open ("/opt/bot/phrases", 'w') as f:
    for i in phrases:
        f.write(i + "\n")

os.popen('systemctl restart bot')
