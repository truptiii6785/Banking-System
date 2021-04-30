import returncus
import newcus


print("                           "+"WELCOME TO PEOPLE'S BANK")
print("                                       " +"We are here to serve")
print('   ')
print('   ')
valid=False
while not valid:
    try:
        choice=int(input("""To open a new bank account, Press 1\n"""+                     
                        """To access your existing account & transact press 2\n"""))
        while choice not in range(1,3) :
            print("Invalid input.Please enter 1/2")
            choice=int(input("""To open a new bank account, Press 1\n"""+                     
                        """To access your existing account & transact press 2\n"""))
        if choice==2:
            returncus.oldacc()
        if choice==1:
            newcus.newacc()
        valid=True
    except ValueError:
        print("Invalid input.Please enter again.")
        
        
        
