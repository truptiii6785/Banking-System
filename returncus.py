import newcus
import random
import time
import sys

def oldacc():
    
    cusnames=[] 
    cuspass=[]
    cusbal=[]
    
    with open("cusnamefile.txt","r") as namefile :
            for line in namefile :
                cusnames.append(line[:-1])
                
    with open("cuspasfile.txt","r") as passfile:
            for line in passfile :
                cuspass.append(line[:-1])
    
    with open("cusbalfile.txt","r") as balfile:
            for line in balfile :
                cusbal.append(line[:-1])
    
    name=input("Enter your name\n")
    if name in cusnames:
        username=name
        userpass=cuspass[cusnames.index(username)]
        bal=float(cusbal[cusnames.index(username)])
        b=bal

    else:
        print("""Sorry\n"""+
               """Looks like you have typed in a wrong name\n"""+
                         """Or dont have an existing account\n""")
        val=False
        while not val:
                    try:
                          ch=int(input("""Enter 1 to re-enter your name\n"""+
                                          """Enter 2 to create a new account\n"""+
                                            """Enter 3 to exit\n"""))
                          while ch not in range(1,4):
                                 print("Invalid input.Please enter(1/2/3)")
                                 ch=int(input("""Enter 1 to re-enter your name\n"""+
                                          """Enter 2 to create a new account\n"""+
                                            """Enter 3 to exit\n"""))
                
                            
                          if ch==1:
                              oldacc()
                          if ch==2:
                              newcus.newacc()
                          if ch==3:
                              print("Thanks for using PEOPLE'S BANK")
                              sys.exit()
                          val=True
                    except ValueError:
                          print("Invalid input.Please re-enter\n")




    
    flag=3
    while flag>0:
         p=input("Please enter your password\n")
         if p==userpass :
             break
         else:
             print("You have entered a wrong password")
             flag=flag-1
             print("You have",flag,"more attempts left")
             
            
    if flag<0:
         print("""Your account has been freezed due to three wrong attempts
                 Please contact your bank for further assistance""")                        
         sys.exit()
         
 
    v=False
    while not v :
        try:
            c=int(input("""Enter 1 to deposit amount\n"""+
                   """Enter 2 to withdraw amount\n"""+
                   """Enter 3 to check balance\n"""))
            if c==1: ###To deposit money in the account
                 l=False
                 while not l:
                     try:
                         n=float(input("Enter the amount to be deposited to the account\n"))
                         bal=bal+n
                         print("The balance available in account after transaction is",bal)
                         l=True
                     except ValueError:
                         print("Invalid input.Please enter again.")
            if c==2: ###To withdraw money from the account
                  e=False
                  while not e:
                     try:
                         d=float(input("Enter the amount to be withdrawn\n"))
                         bal=bal-d
                         print("The balance available in account after transaction is",bal)
                         e=True
                     except ValueError:
                         print("Invalid input.Please enter again.\n")
            if c==3 : ### To check the balance amount
                 print("The balance available in account",bal)
                 print("Thankyou for using PEOPLE'S BANK")
                 exit()
                 
            v=True
        except ValueError:
            print("Invalid input.PLease enter again.\n")
    
           
    cusbal[cusnames.index(username)]=bal
    text=open("cusbalfile.txt","a")
    for i in cusbal:
        text.write(str(i)+"\n")
    text.close()        
            
    ###To generate receipt after bank transaction
    print("                          PEOPLE'S BANK                    ")
    print(" ")
    print("  ")
    print(" ")
    print("TRANSACION DETAILS")
    localtime=time.asctime(time.localtime(time.time()))
    print("Transaction time and date")
    print(localtime)
    print("Account Holder's Name:",username)
    print("Account Balance      :",b)
    if c==1:
        print("Deposit Amount      :",n)
    if c==2:
        print("Withdrawn amount     :",d)
    print("Balance Available     :",bal)
    x=random.randint(1234,537852)
    print("Transaction Number    :",x)
    print("                     ")
    print("                     ")
    print("                     ")
    print("             Thank you for using PEOPLE'S BANK")
    print("                      Visit again             ")
    print("               Retain the transaction receipt ")     
         
         
if __name__=="__main__":
  oldacc()
    

    
