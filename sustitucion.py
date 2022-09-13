from cgitb import handler
from codecs import ascii_encode
from dataclasses import replace
from string import ascii_letters

#txt = input("ingresa tu texto a encriptar: \n")
txt ="hola"
txt2="igsq"
kei = "qwertyuiopasdfghjklzxcvbnm"
def strToAscii(t):
 return [(ord(character)-97) for character in t]
def error(): # cambiar aqui el front-end
    print("please try another key")

def VerifyKey(kei):
    a=kei
    for i in range (97,123):
        a= a.replace(chr(i),"",1)
    if len(a)!=0:
        error()
        return True 
    return False
#lowercase without blanks
def susEncript(txt,kei):
    txt.lower().strip()
    kei.lower().strip()
    if VerifyKey(kei):
        return
    txt= strToAscii(txt)
    askei= strToAscii(kei)
    encript= list(map(lambda c:chr(askei[c]+97),txt)) #chr() de int to ascii
    return "".join(encript)
print(susEncript(txt,kei))

def susDencript(txt,kei):
    txt.lower().strip()
    kei.lower().strip()
    if VerifyKey(kei):
        return
    txt2=""
    for c in txt:
        txt2 += chr(kei.find(c)+97)
    return txt2
print(susDencript(txt2,kei))