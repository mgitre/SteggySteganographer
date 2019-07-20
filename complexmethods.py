import math, PIL, sys, base64
from basicmethods import *
def encode(path, newpath, message: str):
    im = open_image(path).convert('RGBA')
    y = 0
    width, height = im.size
    message += chr(12)
    if len(message) > width * height:
        return 0
    else:
        for i in range(len(message)):
            if i < width:
                x = i
            else:
                x = i % width
                y = math.floor(i / width)
            char = message[i]
            charBin = charToBin(char)
            while len(charBin) < 7:
                charBin = '0' + charBin
            rgba = get_pixel(im, x, y)
            r = list('0' + bin(rgba[0])[2:])
            g = list('0' + bin(rgba[1])[2:])
            b = list('0' + bin(rgba[2])[2:])
            r[-2] = charBin[1]
            r[-1] = charBin[2]
            g[-2] = charBin[3]
            g[-1] = charBin[4]
            b[-2] = charBin[5]
            b[-1] = charBin[6]
            a = 255 - int(charBin[0])
            r = ''.join(r)
            g = ''.join(g)
            b = ''.join(b)
            r = int(r, 2)
            g = int(g, 2)
            b = int(b, 2)
            value = (r, g, b, a)
            pix = im.load()
            pix[x, y] = value
        save_image(im, newpath)
        return 1

def decode(path: str):
    im = open_image(path).convert('RGBA')
    string = ''
    y = 0
    i = 0
    width, height = im.size
    while True:
        if i < width:
            x = i
        else:
            x = i % width
            y = math.floor(i / width)
        rgba = get_pixel(im, x, y)
        r = '0' + bin(rgba[0])[2:]
        g = '0' + bin(rgba[1])[2:]
        b = '0' + bin(rgba[2])[2:]
        a = bin(255 - rgba[3])[2:]
        binny = a[-1] + r[-2] + r[-1] + g[-2] + g[-1] + b[-2] + b[-1]
        try:
            char = chr(int(binny, 2))
            if char == chr(12):
                break
            string += char
        except IndexError:
            continue
        i += 1
    return string    

def encodeFile(path,newpath,filepath):
    filedata=open(filepath,"rb")
    string = bytes.decode(base64.b64encode(filedata.read()))
    filetype=filepath[filepath.index('.'):]
    print(filetype)
    string = filetype+chr(11)+string
    if encode(path,newpath,string) == 0:
        return 0

def encodedFileType(path):
    string = decode(path)
    try:
        place=string.index(chr(11))
    except:
        return 0
        print('except')
    if place >= 20 or len(string) < place-5:
        return 0
        print('place')
    string = decode(path)
    filetype = string[:place]
    return [filetype, string]

def decodeFile(path,filepath,string):
    place=string.index(chr(11))+1
    fileinfo = string[place:]
    byte = str.encode(fileinfo)
    filedata = base64.b64decode(byte)
    file = open(filepath, 'wb')
    file.write(filedata)
