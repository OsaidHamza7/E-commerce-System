from product import Product


class User:
    
    
    users=[]
    def __init__(self, Id: int, Name: str, DateOfBirth,Role:str,Active:int,Basket:dict,Order:int):
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
              f"\t\tUser_DOB:{self.DateOfBirth}\n"
              f"\t\tRole:{self.Role}\n"
              f"\t\tActive:{self.Active}\n"
              f"\t\tBasket:{self.Basket}\n"
              f"\t\tOrder:{self.Order}"
              )
        return "\033[0m"


    def readUsersFile(self):
        file = open("users.txt", "r")
        lines = file.readlines()
        for line in lines:
            L = line.strip().split(";")
            if len(L)==7:
                User_id = int(L[0])
                User_name = str(L[1])
                User_DOB = L[2]
                Role = str(L[3])
                Active = int(L[4])
                Basket = eval(L[5])
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



            else:
                print("the users.txt file is wrong")



    def addUser(self):
        print("Enter The Information Of The User:")
        User_id=int(input("Enter User_id:"))
        User_name= input("Enter User_name:")
        User_DOB=input("Enter User date of birth:")
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


    def displayAllUsers(self):
        for numUser,user in enumerate(self.users):
            print(f"\033[2;91mUser {numUser+1}:\033[0m")
            print(user,end="")
            print("--------------------------------------------")

    def updateUser(self, id):
        for user in self.users:
            if user.Id == id:
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
                    choice = int(input("Enter your choice:\033[0m"))

                    match choice:
                        case 1:
                            user.Name = input("Enter Name:")

                        case 2:
                            user.DateOfBirth= input("Enter DateOfBirth:")

                        case 3:
                            user.Role = int(input("Enter Role:"))

                        case 4:
                            user.Active = int(input("Enter Active:"))

                        case 5:
                            user.Basket = eval(input("Enter Basket:"))

                        case 6:
                            user.Order = int(input("Enter Order:"))

                        case 7:
                            return

                    print("\033[2;92mThe user has been updated successfully\033[0m")

        print("\033[2;91mThe requested user was not found\033[0m")


    def determineRoleUser(self,id):
        for user in self.users:
            if user.Id == id:
                return user.Role

        return None





    def listShoppers(self):

        while True:
            print("\033[2;95m"
                  "Enter an specific criteria that you want :\n"
                  "1.All\n"
                  "2.With items in the basket\n"
                  "3.Has unprocessed orders\n"
                  "4.Requested an order\n"
                  "5.Exit\n"
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
                        if user.Role == "shopper":
                            if len(user.Basket)>0:
                                print(f"\033[2;91mShopper {numShopper}:\033[0m")
                                print(user, end="")
                                print("--------------------------------------------")
                                numShopper+=1

                case 3:
                    numShopper = 1
                    for user in self.users:
                        if user.Role == "shopper":
                            if len(user.Basket) > 0:
                                print(f"\033[2;91mShopper {numShopper}:\033[0m")
                                print(user, end="")
                                print("--------------------------------------------")
                                numShopper += 1

                case 4:
                    numShopper = 1
                    for user in self.users:
                        if user.Role == "shopper":
                            if len(user.Basket) > 0:
                                print(f"\033[2;91mShopper {numShopper}:\033[0m")
                                print(user, end="")
                                print("--------------------------------------------")
                                numShopper += 1

                case 5:

                    return




    def addProductToBasket(self,user_id):
        product_id = int(input("Enter the product_id that you want to add :"))

        if Product.isProductExist(Product,product_id):
            numItems=int(input("Enter number of items from the product you want to add:"))
            for user in self.users:
                if user.Id==user_id:
                    add_product = {product_id: numItems}
                    user.Basket.update(add_product)
                    return
        else:
            print("\033[2;91mThe requested product was not found\033[0m")



   # def displayBasket(self,user_id):

