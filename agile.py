import time

options = ["create new comment", "edit comment", "delete comment", "reply comment"]

   
def main():
    while True:
        user = input('Please enter your name:')
        if not user:
            print("User must have a name")
            break
        password = input('Please enter a password:')
        if not password:
            print("User must have a password")
            break
        
        time.sleep(5)
        greeting = 'Hello, {}! Welcome to Comments-Agile. please login to begin creating posts'.format(user)
    
        print(greeting)

        """
        time.sleep(5)
        for ind, option in enumerate(options):
            print("{}) {}".format(ind+1,option))
            i = input("Enter option: ")
            try:
                if 0 < int(i) <= len(options):
                    return int(i)
            except:
                pass
            return None
        """

        log_user = input('Please enter your account name:')
        log_pass = input('Enter your account password:')

        comment = input('enter new comment:')

    
if __name__ == '__main__':
    main()
