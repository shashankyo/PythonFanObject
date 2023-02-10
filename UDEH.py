class InvalidPin(Exception):
    pass
def verify():
    pin = 9999
    a = int(input("Enter the pin"))
    if pin == a:
        print("Login successfull")
    else:
        try:
            verify()
        except:
             print("2 attemps left")

        try:
            verify()
        except:
            print("1 attempt left")
            
            try:
                verify()
            except:
                print("0 attempts remaining")
                    # print("Login not successfull")
