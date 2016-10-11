import base64
import hashlib
import binascii

def clear_code(code):
    return code[4:-6]

#REDNECK STUFF
decoded = []
decoded.append("stand5")
decoded.append("demons8")
decoded.append("binary2")
decoded.append("maze3")
decoded.append("real7")
decoded.append("me4t4")
decoded.append("h0rs30")
decoded.append("4rt5")
decoded.append("bl0ck5")
decoded.append("sad6")
decoded.append("cow3")
decoded.append("sh3lls4")
decoded.append("land6")
decoded.append("password1")
decoded.append("world4")
decoded.append("crashing")
decoded.append("game9")
decoded.append("c4v35")
decoded.append("url5")
decoded.append("g4mm42")
decoded.append("b4r4")
decoded.append("shortening")
decoded.append("dice9")
decoded.append("esport6")
decoded.append("bon8")
decoded.append("fin1te4")
decoded.append("b34ns1")
decoded.append("roaming7")
decoded.append("t0k3n7")
decoded.append("square7")
decoded.append("winn3r0")
decoded.append("metroc0")
decoded.append("character1")
decoded.append("voyage8")
decoded.append("minimum8")

b64 = input()
b64 = base64.b64decode(b64)
b64 = binascii.b2a_hex(b64).decode('utf-8')

for e in decoded:
    password = "IEEE" + e + "Xtreme"
    password = hashlib.sha256(str.encode(password)).hexdigest()
    if password == b64:
        print(e)
