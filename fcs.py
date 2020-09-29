#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()


a=cgi.FieldStorage()
v=a.getvalue("c")

if (("run" in v or "show" in v or "todays" in v or "date" in v or "Date" in v) and ("date" in v)):
    x=subprocess.getoutput("sudo date")
    print(x)
if (("this month cal" in v) or ("this month calendar" in v) or ("calendar" in v) or ("Cal" in v) or ("Calendar" in v) or ("cal" in v)):
    x=subprocess.getoutput("sudo cal")
    print(x)
if ((("run docker" in v) or ("docker" in v)) and ("version" in v)):
    x=subprocess.getoutput("sudo docker version")
    print(x)
if ((("start" in v) or ("run" in v) or ("open" in v)) and ("firefox" in v)):
    x=subprocess.getoutput("sudo firefox")
    print(x)
if (("show" in v or "running" in v) and ("docker" in v or "container" in v)):
    x=subprocess.getoutput("sudo docker ps")
    print(x)
if (("images" in v or "show" in v) and ("docker" in v or "available container" in v)):
    x=subprocess.getoutput("sudo docker images")
    print(x)
if (("want to launch container" in v or "launch new container" in v)):
    x=subprocess.getoutput("sudo docker run -dit ubuntu:14.04")
    print(x)
if (("want to launch docker as centos:7" in v or "wamt to launch new container as centos:7" in v)):
    x=subprocess.getoutput("sudo docker run -dit centos:7")
    print(x)
if (("stop running docker" in v)):
    x=subprocess.getouput("sudo docker stop ubuntu:14.04")
    print(x)
if ("want to know ip" in v or "ip address" in v or "ping ip" in v):
    x=subprocess.getoutput("sudo ifconfig")
    print(x)
if ("check connection" in v or "connectivity" in v):
    x=subprocess.getoutput("sudo ping -c 4 8.8.8.8")
    print(x)
if ("show me list of files" in v or "show all files" in v):
    x=subprocess.getoutput("sudo ls") 
    print(x)
if (("open" in v or "run" in v or "show" in v or "execute" in v) and ("system info" in v or "system configuration" in v)):
    x=subprocess.getoutput("sudo df -h")
    print(x) 
if ("ram storage" in v or "ram capacity" in v or "used ram space" in v or "show used space of RAM" in v):
    x=subprocess.getoutput("sudo free -m")
    print(x)
if ("show version of python" in v or "python version" in v):
    x=subprocess.getoutput("sudo python3 -V")
    print(x)
else:
    #subprocess("sudo espeak-ng 'have a good day'")
    print("have a good day")
