#!/usr/bin/python3
import time

def introduction():
    print("» Hi!")
    time.sleep(1.7)
    print("» Welcome to the ecryption and decryption program...")
    time.sleep(2.5)
    print("» Loading program...")

introduction()

time.sleep(2)

def loading():
    print("\n")
    for i in range(101):
       time.sleep(0.2)
       i = "«« "+str(i)+"%"+" »»"
       print(i)

loading()

print("\n <Help menu> Available commands: encrypt & decrypt", "\n")


awaiting_input = input(">>> ")

time.sleep(0.5)

cipher = {
    'a': "v07u4tLKinfa",
    'b': "zz45tTn8u4o0",
    'c': "W46tEr10d01z",
    'd': "5aPSCr36quA7",
    'e': "Zg6pPrg17t15",
    'f': "Po84cr3Ud25M",
    'g': "L0l1crXtOO11",
    'h': "7G1CaZ2wBg9f",
    'i': "Z1Yd84we71y3",
    'j': "LL6TRe0yR4tj",
    'k': "kt426ug76Vz3",
    'l': "26IzOZyrXCt4",
    'm': "Z3uj09HJ6Iou",
    'n': "0d2Wna13lERT",
    'o': "N935efQef3JH",
    'p': "7j43Ghnf6R4o",
    'q': "dF13Rw9nX6i8",
    'r': "DOu3fw073r81",
    's': "3C0w23rTg5Ij",
    't': "TE436nyWi5ee",
    'u': "58Ybt78n3e06",
    'v': "39j8rH9TYrcO",
    'w': "0NAtO48veQM7",
    'x': "K2uC2tgEVBn4",
    'y': "9nRm03iH8ECn",
    'z': "8brYHI304ld2",
    'I': "P4ht9871EWG0",
    ')': ")",
    '(': "(",
    '\"': "\"",
    '\'': "\'",
    ',': ",",
    '!': "!",
    '?': "?",
    '.': ".",
    ' ': "5p4CE"
}

def encrypt(x):
    loading()
    print("\n")
    ask = input("»»» Type the text you want do ecrypt: ")
    print("\n»»» Encrypted text:", ' '.join(x[c] for c in ask))
    
reverse_cipher = {v: k for k, v in cipher.items()}

def decrypt(y):
    loading()
    print("\n")
    ask = input("»»» Type the text you want to decrypt: ")
    print("\n»»» Decrypted text:", ''.join(y[x] for x in ask.split()))


if awaiting_input == "help":
   print("\n <Help menu> Available commands: encrypt & decrypt \n")
   awaiting_input = input(">>> ")
elif awaiting_input == "":
     awaiting_input2 == input(">>> ")
elif awaiting_input == "encrypt":
   time.sleep(1)
   encrypt(cipher)
elif awaiting_input == "decrypt":
   time.sleep(1)
   decrypt(reverse_cipher)
else:
   print("<info> Incorrect command")

