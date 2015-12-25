import base64
import binascii

with open('sample') as f:
    out = open('hash.txt', 'w')
    for line in f:
        line = base64.b64decode(line)
        line = binascii.b2a_hex(line)
        line = line.decode('utf-8')
        out.write(line)
        out.write('\n')

    f.close


'''
a = base64.b64decode("tDdmKQpMiVDFA1YdblkHSFzL4Z9UIQ9FSouf3TybOu0=")
a = binascii.b2a_hex(a)
print(a.decode('utf-8'))
'''
