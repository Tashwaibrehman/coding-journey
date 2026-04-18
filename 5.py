print("--- passwrod manager ---")
print("1.register")
print("2.login now")
choice=input("please enter your choice:")
if  choice=="1":
    print("you selected register:")
    username=input("enter username for your registration")
    password=input("enter strong password")
    print("you successfully created acount:",username)
    with open("users.txt","a") as file:
        file.write(username+","+password+"\n")
elif choice=="2":
    print("you selected login")
    username=input("enter username")
    password=input("enter strong password")
    with open("users.txt","r")as file:
        users=file.readlines()
        for user in users:
            stored_user,stord_pswd=user.strip().split(',')
            if stored_user==username and stord_pswd==password:
                print("login successfull")
                site = input("Website: ")
                site_password = input("Password: ")
                with open(username + "_data.txt", "a") as file:
                 file.write(site + ":" + site_password + "\n")
                 with open(username + "_data.txt", "r") as file:
                  print(file.read())
                

                break
        else:
            print("login failed.please try again:")
else:
    print("invalid input.please read instructions carefully and try again.")


