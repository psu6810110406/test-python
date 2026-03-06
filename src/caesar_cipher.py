def caesarCipher(s, k):
    res = ""
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            res += chr(start + (ord(char) - start + k) % 26)
        else:
            res += char
    return res