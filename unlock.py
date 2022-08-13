#!/usr/bin/python3
#defcon30 algo: names, key
#author: kalimax69
#keygen by numinit
#Usage: python3 unlock.py

id = int(input("badge number:")) #badge number
hexcode = [0xa5fa3b7f, 0xe35c2742, 0xbec5ca0f, 0x87e35d46, 0x5acd14f9, 0xabde1fcf]

names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve', 'Trevor']

print("Unlock Codes:")
#algo routine: raises hexcode to the id power, converts result to string,
#rjust to create padding w/zeros for any key less than 10 digits,rotates last char to front

for i in range(len(hexcode)):
    key = str(hexcode[i] ^ id).rjust(10,'0'
