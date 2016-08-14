def helper(message, shift):
    message = message.lower()
    secret = ""
    for c in message:
        if c in "abcdefghijklmnopqrstuvwxyz":
            num = ord(c)
            num += shift
            if num > ord("z"):
                num -= 26
            elif num < ord("a"):
                num += 26
            secret = secret + chr(num)
        else:
            secret = secret + c
    return secret


def encrypt(message):
    return helper(message, 3)


def decrypt(message):
    return helper(message, -3)


# main
print(
    "Welcome to Caepy, python's standalone caesar cipher encrypter and decrypter!\nWritten by Marcos Gómez (http://margobra8.ml/)")
# input("\nPress [ENTER] to launch...\n")
print("\nTIP: If you want to decrypt a message press [ENTER] before entering anything.\n")
msg = input("Your message to encode? ")
if len(msg) > 0:
    # wants to encrypt
    secret = encrypt(msg)
    print("The encoded message is:", secret)
else:
    # empty message; wants to decrypt
    secret = input("Your message to decode? ")
    if len(secret) > 0:
        msg = decrypt(secret)
        print("The decoded message is:", msg)

keep_alive = input("\nPress [ENTER] to exit...\n")
