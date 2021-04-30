import sys
def newacc() :
    name=input("Please enter your name\n")
    
    cusname=[]
    with open("cusnamefile.txt","a+") as namefile: ##to store the name in a text file
            for l in namefile :
                cusname.append(l[:-1])
    cusname.append(name)
    t=open("cusnamefile.txt","a")
    for j in cusname:
         t.write(str(j)+"\n")
    t.close()


    uid=input("Enter your aadhar number\n")
    ad=input("Enter your address\n")
    pan=input("Enter your pan number\n")
    val=False
    while not val:
        try:
            city=int(input("Please select your city\n"+
                           "1.BANGALORE\n"+
                           "2.DELHI\n"+
                           "3.MUMBAI\n"+
                           "4.KOLKATA\n"+
                           "Please enter the corresponding number of the city of your choice\n"))
            while city not in range(1,5):
                print("Invalid input.Please enter(1/2/3/4)")
                city=int(input("Please select your city\n"+
                           "1.BANGALORE\n"+
                           "2.DELHI\n"+
                           "3.MUMBAI\n"+
                           "4.KOLKATA\n"+
                           "Please enter the corresponding number of the city of your choice\n"))
            val=True
        except ValueError:
            print("Invalid input.")
            
    if city==1:
       v=False
       while not v:
        try:
            b=int(input("Please select your nearest branch\n"+
                           "1.Vijaynagar\n"+
                           "2.Banshankari\n"+
                           "3.MG Road\n"+
                           "4.Uttrahalli\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            while b not in range(1,5):
                print("Invalid input.Please enter(1/2/3/4)")
                b=int(input("Please select your nearest branch\n"+
                           "1.Vijaynagar\n"+
                           "2.Banshankari\n"+
                           "3.MG Road\n"+
                           "4.Uttrahalli\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            v=True
        except ValueError:
            print("Invalid input.")
            
            
    if city==3:
       l=False
       while not l:
        try:
            b=int(input("Please select your nearest branch\n"+
                           "1.Andheri\n"+
                           "2.Bandra\n"+
                           "3.Versova\n"+
                           "4.Malbar Hill\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            while b not in range(1,5):
                print("Invalid input.Please enter(1/2/3/4)") 
                b=int(input("Please select your nearest branch\n"+
                           "1.Andheri\n"+
                           "2.Bandra\n"+
                           "3.Versova\n"+
                           "4.Malbar Hill\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            l=True
        except ValueError:
            print("Invalid input.")        
       
             
    if city==2:
       a=False
       while not a:
        try:
            
            b=int(input("Please select your nearest branch\n"+
                           "1.Arjun Nagar\n"+
                           "2.Ajmeri Gate\n"+
                           "3.Dwarka\n"+
                           "4.Hauz Khas\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            while b not in range(1,5):
                print("Invalid input.Please enter(1/2/3/4)") 
                b=int(input("Please select your nearest branch\n"+
                           "1.Arjun Nagar\n"+
                           "2.Ajmeri Gate\n"+
                           "3.Dwarka\n"+
                           "4.Hauz Khas\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            a=True
        except ValueError:
            print("Invalid input.")        
    
    
    if city==4:
       e=False
       while not e:
        try:
            
            b=int(input("Please select your nearest branch\n"+
                           "1.Park Street\n"+
                           "2.Salt Lake\n"+
                           "3.BhawaniPore\n"+
                           "4.Alipore\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            while b not in range(1,5):
                print("Invalid input.Please enter(1/2/3/4)") 
                b=int(input("Please select your nearest branch\n"+
                           "1.Park Street\n"+
                           "2.Salt Lake\n"+
                           "3.Bhawanipore\n"+
                           "4.Alipore\n"+
                           "Please enter the corresponding number of the branch of your choice\n"))
            e=True
        except ValueError:
            print("Invalid input.")    
        
                
    p=input("Enter a password for your new account\n"+
            "The password should contain atleat 4 characters.\n"+
            "Do not disclose your password to anyone.\n")
    if len(p)<4:
         print("Insufficient charcters.Please enter a new password")
         p=input("Enter a password for your new account\n")
    
    cuspass=[]
    with open("cuspasfile.txt","a+") as passfile:
     for line in passfile:
        cuspass.append(line[:-1])
    cuspass.append(p)
    text=open("cuspasfile.txt","a")
    for i in cuspass:
        text.write(str(i)+"\n")
    text.close() 
    
    e=False
    while not e:
        try:
            acc=int(input("""Choose the type of account you wish to open\n"""+
                          """1.Savings Account\n"""+
                          """2.Current Account\n"""+
                          """3.Fixed Deposit\n"""))
            while acc not in range(1,4):
                print("Invalid input.PLease enter(1/2/3)")
                acc=int(input("""Choose the type of account you wish to open\n"""+
                          """1.Savings Account\n"""+
                          """2.Current Account\n"""+
                          """3.Fixed Deposit\n"""))    
            e=True
        except ValueError:
            print("Invalid input.Please enter again")
            
            
    u=False
    while not u:
        try:
            bal=float(input("Please enter the amount you would like to deposit in the account intially\n"))  
            u=True
        except ValueError:
            print("Invalid input.Please enter again")        
                
    cusbal=[]
    with open("cusbalfile.txt","a+") as balfile:
            for q in balfile :
                cusbal.append(q[:-1])
    cusbal.append(bal)
    x=open("cusbalfile.txt","a")
    for k in cusbal:
        x.write(str(k)+"\n")
    x.close()  



    print("Thank you for using PEOPLE'S Bank.Please do visit again")          

if __name__=="__main__":
    newacc()
    
    
