import cv2
import os
import string
# Read the image
img = cv2.imread("flower.jpeg")

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode for encryption: ")

# Create dictionaries for encoding/decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Encode the message into the image
n = 0
m = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3  # To stay within RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.startfile("encryptedImage.jpg")

# Decryption process
message = ""
n = 0
m = 0
z = 0

# Ask for password again for decryption
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
         message += c[img[n, m, z]]
         n += 1
         m += 1
         z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("Incorrect password. Decryption failed.")
