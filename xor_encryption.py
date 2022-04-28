def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    from itertools import cycle
    import base64

    if decode:
        data = data.decode()
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))

    if encode:
        s = xored.encode()
        return base64.encodebytes(s).strip()
    return xored


secret_data = "XOR procedure"

print("The cipher text is")
print(xor_crypt_string(secret_data, encode=True))
print("The plain text fetched")
print(xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True))
