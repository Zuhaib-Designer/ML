set_password = "hero"
for i in range(3):
    # Please Enter your password
    password = input("Enter your password:")

    if set_password == password:
        print("Greeting Professor Falcon")
        break
    else:
        print("Access Denied")

print("Program Finished")
