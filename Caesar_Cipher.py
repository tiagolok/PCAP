# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Caesar cipher - decrypting a message
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    # char = char.upper()
    code = ord(char) + 2
    if code == ord('y')+2:
        code = ord('a')
    if code == ord('z')+2:
        code = ord('b')
        
    cipher += chr(code)

print(cipher)
