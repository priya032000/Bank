#creating bank project-------->
class user():
    usercount = 0
    def __init__(self,f_name,l_name,gender,age):

        self.f_name = f_name.strip().title()
        self.l_name = l_name.strip().title()
        self.gender = gender.strip().title()
        self.age = age
        self.accnumber = "sbi@1"
        
        user.usercount += 1


    def info(self):
        print(f"Name---> {self.f_name} {self.l_name}")
        print(f"Gender---> {self.gender}")
        print(f"Age---> {self.age}")
        print(f"Account number---> {self.accnumber}")


class bank(user):
    def __init__(self,f_name,l_name,gender,age,):
        super().__init__(f_name,l_name,gender,age)
        self.__balance = 0
    def viewbal(self):
        return(f"Your current balance is--> {self.__balance}")

    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return(f"Your diposited amount is---> {amount}")
    
    def withdrawal(self,amount):
        self.__balance = self.__balance - amount
        return(f"Your withdrawal amount is--->{amount}")

    def transfer_amount(self,user,amount):
        if(self.__balance>= amount and amount>=0):
            self.__balance = self.__balance - amount 
            user.__balance = user.__balance + amount
            print("Transfer successful")
        elif self.__balance>=0:
            print("sorry invalid amount")
        else:
            print("can't process insufficent amount")

if(__name__ =="__main__"):

    user1 = bank("Priya","Kalekar","Female",22)
    user2 = bank("Sayali","Kadam","Female",21)
    
    
             
         
        
        

        
      
        
