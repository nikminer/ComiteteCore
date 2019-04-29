from PIL import Image
from PIL import ImageDraw
import os
import Masta

def AddMember(member):
    if not Masta.CheckMember(member.id):
        Masta.AddNewLabmem(member.id)
        CreateFirstWelcomeMessage(member.avatar_url_as(size=128),member.name).save("Maid/src/Images/Temp/"+str(member.id)+".png", format="png")
    else:
        CreatWelcomeMessage(member.avatar_url_as(size=128),member.name).save("Maid/src/Images/Temp/"+str(member.id)+".png", format="png")
        Masta.ReactivateMember(member.id)
    return "Maid/src/Images/Temp/"+str(member.id)+".png"

def LostMember(member):
    CreateLostMessage(member.avatar_url_as(size=128),member.name,member.top_role.name).save("Maid/src/Images/Temp/"+str(member.id)+".png", format="png")
    Masta.DeactivateMember(member.id)
    return "Maid/src/Images/Temp/"+str(member.id)+".png"

def GetTop(members,page):
    mems=[]

    for mem in members:
        template = Image.open('Maid/src/Images/Top.png')

        Avatar = Image.open(GetAvatarFromUrl(mem['mem'].avatar_url_as(size=64)))
        Avatar.thumbnail((64,64))
        template.paste(Avatar,(80,9))
        del Avatar

        AddText(mem['mem'].name,(160, 15),template)
        AddText(mem['data'],(160, 40),template,size=18)

        position=(str(page)+str(len(mems)+1)).rjust(3,'0')
        AddText(position,(6,29),template,color=(255,90,0),size=30,font="BONX-TubeBold.otf")
        
        mems.append(template)

    base=Image.new('RGBA',(template.width,template.height*10),color=(0,0,0,0))

    for i in range(len(members)):
        base.paste(mems[i],(0,0+template.height*i))
    
    path="Maid/src/Images/Temp/top"+str(page)+".png"
    base.save(path)
    return path
    

def CreatWelcomeMessage(memberAvatar,name):
    Avatar = Image.open(GetAvatarFromUrl(memberAvatar))
    base = Image.open('Maid/src/Images/LabmemberReturn.png')
    base.paste(Avatar,(12,11))
    AddText(name,(160, 80),base)
    return base

def CreateFirstWelcomeMessage(memberAvatar,name):
    Avatar = Image.open(GetAvatarFromUrl(memberAvatar))
    base = Image.open('Maid/src/Images/NewLabmember.png')
    base.paste(Avatar,(12,11))
    AddText(name,(160, 80),base)
    return base

def CreateLevelUpMessage(memberAvatar,name,level:str):
    Avatar = Image.open(GetAvatarFromUrl(memberAvatar))
    base = Image.open('Maid/src/Images/LabmemberLevelUP.png')
    #ImageDraw.Draw(Avatar,'RGBA').rectangle([(0,0),(128,128)],fill=(0,255,0,70))
    base.paste(Avatar,(12,11))
    AddText(name,(160, 85),base)
    AddText(level.rjust(3,'0'),(415,30),base,color=(255,90,0),size=30,font="BONX-TubeBold.otf")
    return base


def CreateLostMessage(memberAvatar,name,role):
    Avatar = Image.open(GetAvatarFromUrl(memberAvatar))
    ImageDraw.Draw(Avatar,'RGBA').rectangle([(0,0),(128,128)],fill=(255,0,0,70))
    base = Image.open('Maid/src/Images/LabmemberLost.png')
    base.paste(Avatar,(12,11))
    AddText(name,(160, 65),base)
    AddText(role,(160, 110),base,size=18)
    return base

def AddText(text,position,img,color=(255,255,255),size=22,font='ariblk.ttf'):
    from PIL import ImageFont
    Font = ImageFont.truetype("Maid/src/Fonts/"+font, size)
    ImageDraw.Draw(img).text(position,text,color,font=Font)

def GetAvatarFromUrl(url):
    from io import BytesIO
    from requests import get
    return BytesIO(get(url).content)