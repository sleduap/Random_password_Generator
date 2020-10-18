import string
import random

student_Email = {"sleduap@gmail.com": 6, "sud_led@yahoo.com": 8, "hari@gmail.com": 5}

password_Email = {}
for email_address, length in student_Email.items():
    password_list = []
    for i in range(0, length):
        passcode = random.choice(string.printable)
        password_list.append(passcode)
    password_Email[email_address] = "".join(password_list)
print("Email Address and Corresponding Password of Students")
print("="*100)
print(password_Email)
