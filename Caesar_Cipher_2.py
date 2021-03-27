# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    # char = char.upper()
    code = ord(char) + 2
    if code == ord('y')+2:
        code = ord('a')
    if code == ord('z')+2:
        code = ord('b')
        
    cipher += chr(code)

print(cipher)
