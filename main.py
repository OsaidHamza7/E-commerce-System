
from product import Product
from user import User

if __name__ == '__main__':
    saved_products=False
    saved_users=False
    User.readUsersFile(User)
    Product.readProductsFile(Product)
    if not User.users:
        print("\033[2;91mThere is no users in the system,Please try again\033[0m")
        exit(0)
    print("\033[2;92mThe users loaded from \'users.txt\' file successfully\033[0m")
    print("\033[2;92mThe products loaded from \'products.txt\' file successfully\033[0m")

    User_id = int(input("\033[2;94mPlease Enter The user_id :\033[0m"))
    User_role = User.determineRoleUser(User, User_id)


    while User_role == None:
        print("\033[2;91m\'Access Denied\' the user_id not found,please try again\033[0m")
        User_id = int(input("\033[2;94mPlease Enter The user_id :\033[0m"))
        User_role = User.determineRoleUser(User, User_id)


    while True:
        #_________MENU____________
        print("\033[2;96m\033[2;51m"
              " 1.Add Product\n"
              " 2.Place an item on sale\n"
              " 3.Update product\n"
              " 4.Add a new user\n"
              " 5.Update user\n"
              " 6.Display all users\n"
              " 7.List products\n"
              " 8.List shoppers\n"
              " 9.Add product to the basket\n"
              " 10.Display basket\n"
              " 11.Update basket\n"
              " 12.Place order\n"
              " 13. Execute order\n"
              " 14. Save products to a file\n"
              " 15. Save users to a text file\n"
              " 16.Exit\n"
              )
        choice=int(input("\033[0m\033[2;94mEnter your choice:\033[0m"))

        #________Switch-Case______________
        match choice:

            case 1:
                if User_role=="admin":
                    if not Product.addProduct(Product) :
                        continue
                    print("\033[2;92mThe New Product Has Been Added Successfully\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 2:
                if User_role == "admin":
                    try :
                        Product_ID=int(input("\033[2;94mEnter Product_ID (that you want to place a sale on it) :\033[0m"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of product_id,please try again\033[0m")
                        continue
                    product=Product.isProductExist(Product,Product_ID)
                    if product:
                        Product.saleOfProduct(Product,product)
                    else:
                        print(f"\033[2;91mThe product_id was not found in products,please try again\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")


            case 3:
                if User_role == "admin":
                    try :
                        Product_ID = int(input("\033[2;94mEnter Product_ID (that you want to update):\033[0m"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of product_id,please try again\033[0m")
                        continue
                    product = Product.isProductExist(Product, Product_ID)
                    if product:
                        Product.updateProduct(Product,product)
                    else:
                        print(f"\033[2;91mThe product_id was not found in products,please try again\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 4:
                if User_role == "admin":
                    if not User.addUser(User):
                        continue
                    print("\033[2;92mThe New User Has Been Added Successfully\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")

            case 5:
                if User_role == "admin":
                    try :
                        User_ID = int(input("Enter User_ID (that you want to update) :\033[0m"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of User_ID,please try again\033[0m")
                        continue
                    user = User.isUserExist(User, User_ID)
                    if user:
                        User.updateUser(User, user)
                    else:
                        print(f"\033[2;91mThe product_id was not found in products,please try again\033[0m")
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
                    try:
                        Product_ID = int(input("\033[2;94mEnter Product_ID (that you want to add to the basket) :\033[0m"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of product_id,please try again\033[0m")
                        continue
                    product = Product.isProductExist(Product, Product_ID)
                    if product:
                        User.addProductToBasket(User,User_id,Product_ID)
                    else:
                        print(f"\033[2;91mThe product_id was not found in products,please try again\033[0m")
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")


            case 10:
                if User_role == "shopper":
                    User.displayBasket(User,User_id) # the User_id here for who enter the system
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")
            case 11:
                if User_role == "shopper":
                    User.updateBasket(User, User_id) #the User_id here for who enter the system
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")
            case 12:
                if User_role == "shopper":
                    User.placeOrder(User, User_id)
                else:
                    print("\033[2;91m\'Access Denied\' (Shopper Only)\033[0m")
            case 13 :
                if User_role == "admin":
                    print(User.executeOrder(User))
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")
            case 14:
                if User_role == "admin":
                    Product.saveProductsToFile(Product)
                    saved_products=True
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")
            case 15:
                if User_role == "admin":
                    User.saveUsersToFile(User)
                    saved_users=True
                else:
                    print("\033[2;91m\'Access Denied\' (Admin Only)\033[0m")
            case 16:
                if not saved_users or not saved_products:
                    chos=input("Do ypu want to save products and users first?")
                    if chos.lower()=="yes" or chos.lower()=="y":

                        if not saved_users:
                            User.saveUsersToFile(User)
                        if not saved_products:
                            Product.saveProductsToFile(Product)

                break

            case _:
                print("\033[2;91mThere is no option in this number!!,please try again\033[0m")
