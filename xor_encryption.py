from os import urandom


def generate_key(length: int) -> bytes:
    return urandom(length)


def xor_strings(s, t) -> bytes:
    return bytes([a ^ b for a, b in zip(s, t)])


def encrypt(text, key):
    return xor_strings(text.encode('utf-8'), key)


def decrypt(text, key):
    return xor_strings(text, key).decode('utf-8')


message = input('Type in your message: ')

key = generate_key(len(message))
print('Key: ', key)

cipherText = encrypt(message, key)
print('cipherText: ', cipherText)


print('decrypted: ', decrypt(cipherText, key))


