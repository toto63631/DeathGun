import SATAN2
from SATAN2.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, urllib, string, codecs, requests, ctypes, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = SATAN2.LINE()
cl.nxtQRLogin()
cl.loginResult()

ki = SATAN2.LINE()
ki.nxtQRLogin()
ki.loginResult()

start_runtime = datetime.now()
HelpMessage2 = """
SLC PREMIUM
: BETA
Date : 1/2/2018

- Help
! check Help
- Me
! Your Contact
- Contact
! Opposite Contact
- OpHelp
! check Op Help
- Speed
! check Speed
- Version
! check Version
- Timeleft
! check time left
- Runtime
! check time run
"""
OpMessage = """
SLC PREMIUM
: BETA
Date : 1/2/2018

- Op1
! check Op1 Message
- Op1:(Text)
! set Op1 Message
- Op1:(on/off)
! set Op1 (on/off)

! Op2-3 Coming Soon
"""

Kicker = [cl]
OMG = "0.1.2"
Amid = cl.getProfile()
Creator = "u4c9ac515f9763bea5f4bac3e1a00fa22"
Admin = Amid
ListList = [Amid,Creator]
wait = {
    "AutoAdd":True,
    "message":"THX FOR ADD ME\n\nline.me/ti/p/~esci_",
    "Protection":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "leaveRoom":True,
    "Like":True,
    "Comment":True,
    "CommentText":"THIS IS AUTO LIKE BY\nSATAN\nline.me/ti/p/~esci_",
    "MemberJoin":"Hi",
    "MemberLeave":"Bye",
    "MemberKick":"Wow",
    "Op1":False,
    "Op2":False,
    "Op3":False,
	"lang":"TH",
    "Tag":False,
}

setting1 = {
    "MemberJoin":"Hi"
}

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    global start_runtime
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["AutoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 32:
            if not op.param2 in Kicker:
                if wait["Protection"] == True:
                    try:
                        wait["blacklist"][op.param2] = True
                        G = Kicker.getGroup(op.param1)
                        Kicker.kickoutFromGroup(op.param1,[op.param2])
                        Kicker.inviteIntoGroup(op.param1,[op.param3])
                    except Exception as e:
                       print(e)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.text in ["Me","me"]:
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': Admin}
                cl.sendMessage(msg)

            elif msg.text is None:
                return

            elif msg.text in ["Version","version"]
                cl.sendText(msg.to,OMG)

            elif msg.text in ["Hp","Help","คำสั่ง"]:
                nowTimeis = datetime.now()
                nowH = datetime.strftime(nowTimeis,"%H")
                nowM = datetime.strftime(nowTimeis,"%M")
                nowS = datetime.strftime(nowTimeis,"%S")
                tm = "\nNow : "+nowH+":"+nowM+":"+nowS
                HelpMessage = """
SLC PREMIUM
: BETA
Date : 1/2/2018"""+tm+"""

- Help
! check Help
- Me
! Your Contact
- Contact
! Opposite Contact
- OpHelp
! check Op Help
- Speed
! check Speed
- Version
! check Version
- Timeleft
! check time left
- Runtime
! check time run
"""
                cl.sendText(msg.to,HelpMessage)

            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)

            elif msg.text in ["Sp","sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to,"กรุณารอสักครู่...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to,"[ %s วินาที ]\n[ ปิง : " % (elapsed_time) + str(int(round((time.time() - start) * 896)))+" ms ]")

            elif 'Op1:' in msg.text.lower():
                try:
                    search = msg.text.lower().replace("Op1:","")
                    cl.sendText(msg.to,"กำลังเซ็ต Op1")
                except:
                    try:
                        setting1["MemberJoin"] = search
                        cl.sendText(msg.to,"Set Op1 to "+setting1["MemberJoin"])
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif msg.text in ["Op1: "]:
                search = msg.text.replace("Op1: ","")
                try:
                    setting1["MemberJoin"] = search
                    cl.sendText(msg.to,".")
                except:
                    pass
			elif msg.text in ["Execpt in"]:
				G = cl.getGroup

            elif msg.text in ["Op1"]:
                if wait["lang"] == "TH":
                    Op1Message = setting1["MemberJoin"]
                    cl.sendText(msg.to,Op1Message)

            elif msg.text in ["Op1:on","Op1 on"]:
                if wait["lang"] == "TH":
                    if wait["Op1"] == False:
                        wait["Op1"] = True
                        cl.sendText(msg.to,"เปืด Op1 เรียบร้อยแล้ว")
                    else:
                        if wait["Op1"] == True:
                            cl.sendText(msg.to,"Op1 เปืดอยู่แล้ว")
            elif msg.text in ["Op1:off","Op1 off"]:
                if wait["lang"] == "TH":
                    if wait["Op1"] == True:
                        wait["Op1"] = False
                        cl.sendText(msg.to,"ปืด Op1 เรียบร้อยแล้ว")
                    else:
                        if wait["Op1"] == False:
                            cl.sendText(msg.to,"Op1 ปืดอยู่แล้ว")

            elif msg.text in ["Like:on","Like on"]:
                if wait["lang"] == "TH":
                    if wait["Like"] == False:
                        wait["Like"] = True
                        cl.sendText(msg.to,"เปิด Auto Like เรียบร้อยแล้ว")
                    else:
                        if wait["Like"] == True:
                            cl.sendText(msg.to,"Auto Like เปืดอยู่แล้ว")

            elif msg.text in ["Comment:on","Comment on"]:
                if wait["lang"] == "TH":
                    if wait["Comment"] == False:
                        wait["Comment"] = True
                        cl.sendText(msg.to,"เปิด Comment เรียบร้อยแล้ว")
                    else:
                        if wait["Comment"] == True:
                            cl.sendText(msg.to,"Comment เปืดอยู่แล้ว")

            elif msg.text in ["Like:off","Like off"]:
                if wait["lang"] == "TH":
                    if wait["Like"] == True:
                        wait["Like"] = False
                        cl.sendText(msg.to,"ปิด Auto Like เรียบร้อยแล้ว")
                    else:
                        if wait["Like"] == False:
                            cl.sendText(msg.to,"Auto Like ปืดอยู่แล้ว")

            elif msg.text in ["Comment:off","Comment off"]:
                if wait["lang"] == "TH":
                    if wait["Comment"] == True:
                        wait["Comment"] = False
                        cl.sendText(msg.to,"ปิด Comment เรียบร้อยแล้ว")
                    else:
                        if wait["Comment"] == False:
                            cl.sendText(msg.to,"Comment ปืดอยู่แล้ว")
            elif msg.text.lower() == "Timeleft":
                cl.sendText(msg.to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" Hour, "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" Minute, "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" second,")
            elif msg.text.lower() == "Runtime":
                cl.sendText(msg.to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" Hour, "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" Minute, "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" second,")
        if op.type == 17:
            if wait["Op1"] == True:
                Op1Message = wait["MemberJoin"]
                cl.sendText(op.param1,Op1Message)

        if op.type == 15:
            if wait["Op2"] == True:
                pass

        if op.type == 19:
            if wait["Op3"] == True:
                pass

    except Exception as e:
        ki.sendText(msg.to,(e))

def TYPE26(op):
    global Kicker
    global ListList
    try:
        if op.type == 26:
            msg = op.message
            if msg.text in ["Me","me",".me",".Me"]:
                Satan = msg.from_
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': Satan}
                cl.sendMessage(msg)
            if 'MENTION' in list(msg.contentMetadata.keys()) != None:
                 if wait["Tag"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + " !"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break
            if msg.text in ["Version","version"]:
                cl.sendText(msg.to,OMG)
    except Exception as e:
        ki.sendText(msg.to,(e))

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["Like"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["Comment"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["CommentText"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()

try:
    def TYPE26DOING():
        try:
            while True:
                try:
                    Ops = cl.fetchOps(ac.Poll.rev, 5)
                except EOFError:
                    raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
                for Op in Ops:
                    if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                        clac.Poll.rev = max(cl.Poll.rev, Op.revision)
                        TYPE26(op)
        except:
            pass
    thread2 = threading.Thread(target=helper3run)
    thread2.daemon = True
    thread2.start()
except:
    pass

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
