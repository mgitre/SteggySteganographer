def xor(plaintext, n):
    #plaintext = input('Input Text: ')
    asciiText = []
    if len(plaintext) % 2 != 0:
        plaintext+='.'
    for char in plaintext:
        letBin = bin(ord(char))[2:]
        while(len(letBin) < 7):
            letBin = '0' + letBin
        asciiText.append(letBin)
    binText = ''.join(asciiText)
    encryptedText = ''
    for i in range(n):
        for char in range(len(binText)):
            if char == 0:
                encryptedText += binText[1]
            elif char == len(binText) - 1:
                encryptedText += binText[-2]
            else:
                encryptedText += str(int(binText[char - 1]) ^ int(binText[char + 1]))
        binText = encryptedText
        encryptedText = ''
    encryptedAscii=''
    for i in range(int(len(binText)/7)):
        sevenbits=binText[7*i:7*(i+1)]
        encryptedAscii+=chr(int(sevenbits,2))
    return encryptedAscii

def rxor(ciphertext, n):
    binary = ''
    rxored = []
    for char in ciphertext:
        binno = bin(ord(char))[2:]
        while len(binno) < 7:
            binno = '0'+binno
        binary += binno
    for i in range(len(binary)):
        rxored.append('')
    for i in range(n):
        rxored[1] = boolToNum(int(binary[0]))
        rxored[-2] = boolToNum(int(binary[-1]))
        for i in range(int((len(binary) - 2) / 2)):
            pos = 2 * i + 3
            if int(binary[pos - 1]):
                rxored[pos] = boolToNum(not int(rxored[pos - 2]))
            else:
                rxored[pos] = rxored[pos - 2]
        for i in range(int((len(binary) - 2) / 2)):
            pos = (len(binary) - 4) - 2 * i
            if int(binary[pos + 1]):
                rxored[pos] = boolToNum(not int(rxored[pos + 2]))
            else:
                rxored[pos] = rxored[pos + 2]
        binary = ''.join(rxored)
    encryptedAscii=''
    for i in range(int(len(binary)/7)):
        sevenbits=binary[7*i:7*(i+1)]
        encryptedAscii+=chr(int(sevenbits,2))
    return encryptedAscii

def boolToNum(booleanBoio):
    if isinstance(booleanBoio, str):
        return str(booleanBoio)
    else:
        if booleanBoio:
            return '1'
        else:
            return '0'

plain = input("Text is yay: ")
print(xor(plain,1))
xored = input("It is xored: ")
print(rxor(xored,1))
