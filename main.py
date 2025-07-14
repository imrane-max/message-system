import os
import time
import random

# جدول التحويل
char_map = {
    "a": 1, "z": 2, "e": 3, "r": 4, "t": 5,
    "y": 6, "u": 7, "i": 8, "o": 9, "p": 10,
    "q": 11, "s": 12, "d": 13, "f": 14, "g": 15,
    "h": 16, "j": 17, "k": 18, "l": 19, "m": 20,
    "w": 21, "x": 22, "c": 23, "v": 24, "b": 25,
    "n": 26
}

# توليد المفتاح
key1 = random.randint(10000000, 99999999)
key2 = key1  # نجعل المفتاح الثاني هو نفسه الأول

print("*** Person 1 ***")
user = input("Message: ")

# التشفير
converted = []
for char in user:
    if char.lower() in char_map:
        converted.append(str(char_map[char.lower()]))
    else:
        converted.append(char)

# عرض الرسالة المشفرة والمفتاح
print("\nEncrypted:", " ".join(converted))
print("Your secret key is:", key1)

# الانتظار قبل مسح الشاشة
time.sleep(5)
os.system("clear")  # لمسح الشاشة

# الشخص الثاني
print("*** Person 2 ***")

if key2 == key1:
    print(f"The message was: {user}")
else:
    print("Wrong key. Access denied.")
