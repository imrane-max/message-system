import os

elementes_for_password = [".", " "]

cemail = input("email:")

def check_prassword():
    
    

    for reapt in range(3):
        password = input("password:")
        for elemente in password:
            if elemente in elementes_for_password:
                print("error")
                return  # توقف الفانكشن فقط
        os.system("clear")


check_prassword()
