"""simple encrpytion and decryption of text
asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25
prints out the encoded text."""

import pyinputplus as pyip

# Get the message and the code shift and validate them
text = pyip.inputStr('Please enter your message: ')
while True:
    shift = pyip.inputInt('Please enter a number between 0 and 25 to encode by: ')
    if shift < 0 or  shift > 25:
        print('Sorry, it must be between 0 and 25.')
        continue
    break

cypher = ''

for character in text:
    # if not an alphabetic character, disregard it.
    if not character.isalpha():
        cypher += character
        continue
    # Treat upper and lower cases as separate codes

    ascii_char = ord(character)
    ascii_char += shift

    if (character.isupper() and ascii_char > 90) or ascii_char > 122:
        ascii_char -= 25

    cypher += (chr(ascii_char))

print(cypher)

# check if user wants to decypher message
decypher = pyip.inputYesNo('\nDo you want to decypher the message now?')

if not decypher:
    quit()

decypher = ''
for character in cypher:
    if not character.isalpha():
        decypher += character
        continue

    ascii_char = ord(character)
    ascii_char -= shift

    if (character.isupper() and ascii_char < 65) or character.islower() and ascii_char < 97:
        ascii_char += 25

    decypher += (chr(ascii_char))

print(decypher)
