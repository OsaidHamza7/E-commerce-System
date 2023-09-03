
class Product:

    products=[]


    def __init__(self, Id:int, Name:str, Category:str, Price:int, Inventory:int, Supplier:str, Has_on_offer:int,Offer_price:int,Valid_until):
        self.Id = Id
        self.Name = Name
        self.Category = Category
        self.Price = Price
        self.Inventory = Inventory
        self.Supplier = Supplier
        self.Has_on_offer = Has_on_offer
        self.Offer_price = Offer_price
        self.Valid_until = Valid_until


    def __str__(self):
        print(f"\033[2;93m\t\tProduct_id:{self.Id}\n"
              f"\t\tProduct_name:{self.Name}\n"
              f"\t\tProduct_category:{self.Category}\n"
              f"\t\tPrice:{self.Price}\n"
              f"\t\tInventory:{self.Inventory}\n"
              f"\t\tSupplier:{self.Supplier}\n"
              f"\t\tHas_on_offer:{self.Has_on_offer}"
              )

        if self.Has_on_offer:
            print(f"\t\tOffer_price:{self.Offer_price}\n"
                  f"\t\tValid_until:{self.Valid_until}"
                  )
        return "\033[0m"

    def readProductsFile(self):
        file = open("products.txt", "r")
        lines = file.readlines()
        for line in lines:
            L = line.strip().split(";")
            if len(L)==9:
                Product_id = int(L[0])
                Product_name = str(L[1])
                Product_category = str(L[2])
                Price = int(L[3])
                Inventory = int(L[4])
                Supplier = str(L[5])
                Has_on_offer = int(L[6])
                Offer_price = int(L[7])
                Valid_until = str(L[8])

                p = Product(Product_id,
                            Product_name,
                            Product_category,
                            Price,
                            Inventory,
                            Supplier,
                            Has_on_offer,
                            Offer_price,
                            Valid_until
                            )

                self.products.append(p)

            else:
                print("the products.txt file is wrong")

    def addProduct(self):
        print("Enter The Information Of The Product:")
        Product_id=int(input("Enter Product_id:"))
        Product_name= input("Enter Product_name:")
        Product_category=input("Enter Product_category:")
        Price = int(input("Enter Price:"))
        Inventory = int(input("Enter Inventory:"))
        Supplier = input("Enter Supplier:")
        Has_on_offer = int(input("Enter Has_on_offer:"))
        Offer_price=None
        Valid_until=None

        if Has_on_offer:
            Offer_price = int(input("Enter Offer_price:"))
            Valid_until = input("Enter Valid_until:")

        p= Product( Product_id,
                    Product_name,
                    Product_category,
                    Price,
                    Inventory,
                    Supplier,
                    Has_on_offer,
                    Offer_price,
                    Valid_until
                    )

        self.products.append(p)


    def listProducts(self):

        while True:
            print("\033[2;95m"
                  "Enter an specific criteria that you want :\n"
                  "1.All\n"
                  "2.Offers\n"
                  "3.Category\n"
                  "4.Name\n"
                  "5.Exit\n"
                  )
            choice = int(input("Enter your choice:\033[0m"))
            match choice:

                case 1:
                    for numProduct, product in enumerate(self.products):
                        print(f"\033[2;91mProduct {numProduct + 1}:\033[0m")
                        print(product, end="")
                        print("--------------------------------------------")

                case 2:
                    numProduct=1
                    for product in self.products:

                        if product.Has_on_offer==1:
                            print(f"\033[2;91mProduct {numProduct}:\033[0m")
                            print(product, end="")
                            print("--------------------------------------------")

                            numProduct+=1

                case 3:
                    category=input("Enter the name of the category :")

                    numProduct = 1
                    for product in self.products:

                        if product.Category == category:
                            print(f"\033[2;91mProduct {numProduct}:\033[0m")
                            print(product, end="")
                            print("--------------------------------------------")

                            numProduct += 1

                case 4:
                    name = input("Enter the name of the product :")
                    numProduct = 1
                    for product in self.products:
                        if product.Name == name:
                            print(f"\033[2;91mProduct {numProduct}:\033[0m")
                            print(product, end="")
                            print("--------------------------------------------")
                            numProduct += 1
                case 5:
                    return


    def saleOfProduct(self,id):
        for product in self.products:
            if product.Id==id:
                product.Has_on_offer=1
                product.Offer_price = int(input("Enter Offer_price:"))
                product.Valid_until = input("Enter Valid_until:")
                print("\033[2;92mThe discount has been added to the product successfully\033[0m")
                return
        print("\033[2;91mThe requested product was not found\033[0m")


    def updateProduct(self,id):
        for product in self.products:
            if product.Id==id:
                while True:
                    print("\033[2;95m"
                          "Enter an option that you want to update:\n"
                          "1.Name\n"
                          "2.Category\n"
                          "3.Price\n"
                          "4.Inventory\n"
                          "5.Supplier\n"
                          "6.Has_on_offer\n"
                          "7.Offer_price\n"
                          "8.Valid_until\n"
                          "9.Exit\n"
                          )
                    choice = int(input("Enter your choice:\033[0m"))

                    match choice:
                        case 1:
                            product.Name= input("Enter Name:")

                        case 2:
                            product.Category = input("Enter Category:")

                        case 3:
                            product.Price = int(input("Enter Price:"))

                        case 4:
                            product.Inventory = int(input("Enter Inventory:"))

                        case 5:
                            product.Supplier = input("Enter Supplier:")

                        case 6:
                            product.Has_on_offer = int(input("Enter Has_on_offer:"))

                        case 7:
                            if product.Has_on_offer:
                                product.Offer_price = int(input("Enter Offer_price:"))
                                break
                            print("\033[2;91mYou can't update this feature until update \"Has_on_offer\" to 1\033[0m")

                        case 8:
                            if product.Has_on_offer:
                                product.Valid_until = input("Enter Valid_until:")
                                break
                            print("\033[2;91mYou can't update this feature until update \"Has_on_offer\" to 1\033[0m")
                        case 9:
                            return

                    print("\033[2;92mThe product has been updated successfully\033[0m")


        print("\033[2;91mThe requested product was not found\033[0m")


    def isProductExist(self,id):
        for product in self.products:
            if product.Id == id:
                return True
        return False