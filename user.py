from product import Product
from datetime import datetime

class User:

    
    users=[]
    def __init__(self, Id: int, Name: str, DateOfBirth:datetime.date,Role:str,Active:int,Basket:dict,Order:int):
        self.Id = Id
        self.Name = Name
        self.DateOfBirth = DateOfBirth
        self.Role = Role
        self.Active = Active
        self.Basket = Basket
        self.Order = Order

    def __str__(self):
        print(f"\033[2;93m\t\tUser_id:{self.Id}\n"
              f"\t\tUser_name:{self.Name}\n"
              f"\t\tUser_DOB:{self.DateOfBirth.strftime('%x')}\n"
              f"\t\tRole:{self.Role}\n"
              f"\t\tActive:{self.Active}\n"
              f"\t\tBasket:{self.Basket}\n"
              f"\t\tOrder:{self.Order}"
              )
        return "\033[0m"

    def readUsersFile(self):
        self.users=[]
        file = open("users.txt", "r")
        lines = file.readlines()
        for num,line in enumerate(lines):
            L = line.strip().split(";")
            if len(L)==7:
                try :
                    User_id = int(L[0])
                    User_name = str(L[1])
                    User_DOB = (datetime.strptime(L[2],'%m/%d/%Y')).date()
                    Role = str(L[3])
                    Active = int(L[4])
                    Basket = {}
                    b=L[5]
                    if len(b) > 2:
                        b=b[1:-1].split(',')
                        for i in b:
                            product_id, numItems=i.split(':')
                            Basket.__setitem__(int(product_id),int(numItems))
                    Order = int(L[6])

                    u = User(User_id,
                             User_name,
                             User_DOB,
                             Role,
                             Active,
                             Basket,
                             Order
                             )

                    self.users.append(u)

                except ValueError:
                    print(f"\033[2;91mValueError in \'users.txt\' file:There is invalid input value in line {num+1},please check your text file and you can try again.\033[0m")


            else:
                print(f"\033[2;91mFormatError found in \'users.txt\' file:The number of features must be 7 in line {num+1},please check your text file and you can try again.\033[0m")

    def isUserExist(self,user_id):
        for user in self.users:
            if user.Id == user_id:
                return user
        return None

    def addUser(self):
        print("Please Fill The Information Of The User :")
        try :
            User_id=int(input("Enter User_id:"))
            if self.isUserExist(self, User_id):
                print(f"\033[2;91mThe User_id was found in users,please try again\033[0m")
                return
            User_name = input("Enter User_name:")
            User_DOB =(datetime.strptime(input("Enter DateOfBirth:"),'%m/%d/%Y')).date()
            Role = input("Enter Role:")
            Active = int(input("Enter Active:"))
            Basket = eval(input("Enter Basket:"))
            Order = int(input("Enter Order:"))


            u= User( User_id,
                        User_name,
                        User_DOB,
                        Role,
                        Active,
                        Basket,
                        Order
                        )

            self.users.append(u)
        except ValueError:
            print(f"\033[2;91mValueError:please enter a valid values\033[0m")
            return False
        return True

    def displayAllUsers(self):
        for numUser,user in enumerate(self.users):
            print(f"\033[2;91mUser {numUser+1}:\033[0m")
            print(user,end="")
            print("--------------------------------------------")

    def updateUser(self, user):
        while True:
            print("\033[2;95m"
                  "Enter an option that you want to update:\n"
                  "1.Name\n"
                  "2.DateOfBirth\n"
                  "3.Role\n"
                  "4.Active\n"
                  "5.Basket\n"
                  "6.Order\n"
                  "7.Exit\n"
                  )
            choice = int(input("Enter an option that you want to update:\033[0m"))

            match choice:
                case 1:
                    try:
                        user.Name = input("Enter Name:")
                    except ValueError:
                        print(f"\033[2;91mInvalid value of name,please try again\033[0m")
                        continue
                case 2:
                    try:
                        user.DateOfBirth= (datetime.strptime(input("Enter DateOfBirth:"),'%m/%d/%Y')).date()
                    except ValueError:
                        print(f"\033[2;91mInvalid value of DateOfBirth,please try again\033[0m")
                        continue
                case 3:
                    try:
                        user.Role = input("Enter Role:")
                    except ValueError:
                        print(f"\033[2;91mInvalid value of role,please try again\033[0m")
                        continue
                case 4:
                    try:
                        user.Active = int(input("Enter Active:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of active,please try again\033[0m")
                        continue
                case 5:
                    try:
                        user.Basket = eval(input("Enter Basket:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of basket,please try again\033[0m")
                        continue
                case 6:
                    try:
                        user.Order = int(input("Enter Order:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of order,please try again\033[0m")
                        continue
                case 7:
                    return
                case _:
                    print("\033[2;91mThere is no option in this number!!,please try again\033[0m")

            print("\033[2;92mThe user has been updated successfully\033[0m")

    def determineRoleUser(self,user_id):
        user=self.isUserExist(self,user_id)
        if user:return user.Role
        return None

    def listShoppers(self):
        while True:
            print("\033[2;95m"
                  "Enter an specific criteria that you want :\n"
                  "1.All\n"
                  "2.With items in the basket\n"
                  "3.Has unprocessed orders\n"
                  "4.Exit\n"
                  )
            choice = int(input("Enter your choice:\033[0m"))
            match choice:

                case 1:
                    numShopper=1
                    for user in self.users:
                        if user.Role=="shopper":
                            print(f"\033[2;91mShopper {numShopper}:\033[0m")
                            print(user, end="")
                            print("--------------------------------------------")
                            numShopper+=1
                case 2:
                    numShopper = 1
                    for user in self.users:
                        if user.Role == "shopper" and len(user.Basket)>0:
                            print(f"\033[2;91mShopper {numShopper}:\033[0m")
                            print(user, end="")
                            print("--------------------------------------------")
                            numShopper+=1
                case 3:
                    numShopper = 1
                    x=0
                    for user in self.users:
                        if user.Role == "shopper" and user.Order:
                            print(f"\033[2;91mShopper {numShopper}:\033[0m")
                            print(user, end="")
                            print("--------------------------------------------")
                            numShopper += 1
                            x+=1
                    if not x:
                        print("\033[2;91mThere is no shoppers have unprocessed orders.\033[0m")

                case 4:
                    return
                case _:
                    print("\033[2;91mThere is no option in this number!!,please try again\033[0m")

    def addProductToBasket(self,user_id,product_id):
        numItems=int(input("Enter number of items from the product you want to add:"))
        user=self.isUserExist(self,user_id)
        add_product = {product_id: numItems}
        user.Basket.update(add_product)
        return


    def displayBasket(self,user_id):
       user=self.isUserExist(self,user_id) #the user is exist always becasue he who entered the systen
       if len(user.Basket) > 0:
           numProduct = 1
           total_cost=0
           for product_id,num_items in user.Basket.items():
               print(f"\033[2;91mProduct {numProduct}:\033[0m")
               product_price=Product.displayProduct(Product,product_id)
               if product_price:
                   cost=num_items*product_price # ( product_price = product_price - Offer_Price )
                   total_cost+=cost
                   print(f"\t\t\033[2;93mNumber of items = {num_items}")
                   print(f"\t\tCost of purchase of the product = {cost}\033[0m")
               else:
                   print(f"\033[2;91mThe product was not found (there is no product with this id {product_id} )\033[0m")
               print("--------------------------------------------")
               numProduct += 1

           print(f"\033[2;92m\t\tBasket Cost = {total_cost}\033[0m")

       else:
           print("\033[2;91mThere is nothing in the basket\033[0m")



    def updateBasket(self,user_id):
        while True:
            print("\033[2;95m"
                  "Enter an specific criteria that you want :\n"
                  "1.Clear\n"
                  "2.Remove\n"
                  "3.Update\n"
                  "4.Exit\n"
                  )
            choice = int(input("Enter your choice:\033[0m"))
            user=self.isUserExist(self,user_id) #the User_id here for who enter the system
            match choice:
                case 1:
                    user.Basket.clear()
                    break

                case 2:
                    proudct_id=int(input("Enter the product_id to remove :"))
                    try :
                        user.Basket.pop(proudct_id)
                        print("\033[2;91mThe product was removed successfully\033[0m")
                    except KeyError:
                        print("\033[2;91mThe product was not found in the products\033[0m")
                    break
                case 3:
                    proudct_id = int(input("Enter the product_id to update :"))
                    if proudct_id in user.Basket:
                        number_items=int(input("Enter number of items :"))
                        user.Basket[proudct_id]=number_items
                        print("\033[2;91mThe product was updated successfully\033[0m")

                    else:
                        print("\033[2;91mThe product was not found in the basket\033[0m")
                    break

                case 4:
                    return
                case _:
                    print("\033[2;91mThere is no option in this number!!,please try again\033[0m")

    def placeOrder(self,user_id):
        user = self.isUserExist(self, user_id)
        if user:
            user.Order=1

    def executeOrder(self):
        shopper_id=int(input("Enter shopper_id to execute his order :"))
        for user in self.users:
            if user.Id==shopper_id:
                for product_id ,numItems in user.Basket.items():
                    if not Product.deductItemsOfProduct(Product,product_id,numItems):
                        print(f"\033[2;91mNote:The Product ID {product_id} in the shopper basket not found in products.\033[0m")
                user.Basket.clear()
                return "\033[2;92mThe Order Executed successfully\033[0m"
        return "\033[2;91mThe shopper with entered ID not found!\033[0m"

    def saveUsersToFile(self):
        fileName=input("Enter a file where you want to save the users data:")
        while not fileName.endswith(".txt"):
            fileName = input("\033[2;91mError!,Please enter a valid filename(.txt) :\033[0m")
        file = open(fileName, "w")
        for user in self.users:
            file.write(f"{user.Id};{user.Name};{user.DateOfBirth};{user.Role};{user.Active};{str(user.Basket)};{user.Order}")
            file.write("\n")
        print(f"\033[2;91mThe users data was saved successfully in the {fileName} file.\033[0m")
