import hashlib as hl
user = "admin123"
#hasło to hash z programu generator haseł - dla hasła ccbot hash to 1abe495789f41bce4484339116aa7085ad466fde2d3a938a3c8684820d95904e
password = "1abe495789f41bce4484339116aa7085ad466fde2d3a938a3c8684820d95904e"
dane="false"
while dane == "false":
    inp_user=str(input("Podaj użytkownika "))
    inp_password=str(input("Podaj hasło "))
    hash_password=hl.sha256(inp_password.encode()).hexdigest()
    if inp_user != user:
        print("Error 1, podany użytkownik nie jest poprawny")
    elif hash_password != password:
        print("Error 2, podane hasło nie jest poprawne")
    else:
        dane="true"
print("Dane logowania poprawne")