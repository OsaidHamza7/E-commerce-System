
from product import Product
from user import User

if __name__ == '__main__':


    User.readUsersFile(User)
    Product.readProductsFile(Product)

    User_id = int(input("Please Enter The user_id :"))
    User_role = User.determineRoleUser(User, User_id)


    while User_role == None:
        print("\033[2;91m\'Access Denied\' the user_id not found\033[0m")
        User_id = int(input("Please Enter The user_id :"))
        User_role = User.determineRoleUser(User, User_id)


    while True:
        #_________MENUE____________
        print("\033[2;96m"
              "Enter an option :\n"
              "1.Add Product\n"
              "2.Place an item on sale\n"
              "3.Update product\n"
              "4.Add a new user\n"
              "5.Update user\n"
              "6.Display all users\n"
              "7.List products\n"
              "8.List shoppers\n"
              "16.Exit\n"
              )
        choice=int(input("Enter your choice:\033[0m"))

        #________Switch-Case______________
        match choice:

            case 1:
                if User_role=="admin":
                    Product.addProduct(Product)
                    print("\033[2;92mThe New Product Added Successfully\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 2:
                if User_role == "admin":
                    print("Enter A Product that you want to place a sale on it:")
                    Product_ID=int(input("Enter the Id of the product:"))
                    Product.saleOfProduct(Product,Product_ID)
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 3:
                if User_role == "admin":
                    print("Enter A Product that you want to update:")
                    Product_ID = int(input("Enter the Id of the product:"))
                    Product.updateProduct(Product, Product_ID)
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 4:
                if User_role == "admin":
                    User.addUser(User)
                    print("\033[2;92mThe New User Added Successfully\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 5:
                if User_role == "admin":
                    print("Enter A User that you want to update:")
                    User_ID = int(input("Enter the Id of the user:"))
                    User.updateUser(User, User_ID)
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 6:
                if User_role == "admin":
                    print("\033[2;92mDisplay All Users :\033[0m")
                    User.displayAllUsers(User)
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 7:
                Product.listProducts(Product)

            case 8:
                if User_role == "admin":
                    User.listShoppers(User)
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 9:
                if User_role == "shopper":

                    User.addProductToBasket(User,User_id)
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")

            case 10:
                if User_role == "shopper":
                    User.displayBasket(User,User_id)
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")




            case 16:
                break

