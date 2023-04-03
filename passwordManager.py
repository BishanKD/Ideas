def password_manager():
    passwords = {}
    masterpw = input("Enter master password: ")
    if(masterpw=="bishan"):
        def pwd():
            start = input("Access stored passwords(S) or Add new password(N): ")
            if(start=="S"):
                for keys, value in passwords.items():
                    print(keys+": "+ value)
            elif(start=="N"):
                name = input("Enter username: ")
                if name in passwords.keys():
                    print("Already exists")
                    pwd()
                else:
                    password = input("Enter password: ") 
                    passwords.update({name:password}) 
                    print("Stored!")
                    pwd()
            else:
                print("Invalid input")
                pwd()
        pwd()              
    else:
        print("Wrong password.")
        password_manager()

password_manager()

