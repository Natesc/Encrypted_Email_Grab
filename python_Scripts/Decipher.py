def encrypt(text, shift):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isupper() and char is not " ":
            result += chr((ord(char) + shift-65) % 26 + 65)
        elif char is " ":
            result += char
        else:
            result += chr((ord(char) + shift-97) % 26 +97)
    return result
