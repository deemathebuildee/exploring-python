""" 
the notes in this program are for the sole purpose
of improving and clarifying because im new to Python.
it doesnt mean that any ai was used to write this program.

What this program does:
Asks the user for a file name
Reads the file's contents as bytes
Makes a SHA-256 hash (a fingerprint) of those bytes
Prints the fingerprint
"""

import hashlib


file = input("Enter your file here (WITHOUT QUTES!): ")
with open (file, "rb") as f: #with X as f it closes the file automatically when the indented part ends
    data = f.read() #reads everything in the file, and we store it in the variable data


fingerprint = hashlib.sha256(data).hexdigest() #sha256(data) makes the fingerprint from the bytes 
# .hexdigest() turns it into a readable thing for us
print(fingerprint)
