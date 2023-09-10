from datetime import datetime
class Product:
    products=[]
    def __init__(self, Id:int, Name:str, Category:str, Price:int, Inventory:int, Supplier:str, Has_on_offer:int,Offer_price:int,Valid_until:datetime.date):
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
                  f"\t\tValid_until:{ self.Valid_until.strftime('%x')}"
                  )
        return "\033[0m"

    def readProductsFile(self):
        self.products=[]
        file = open("products.txt", "r")
        lines = file.readlines()
        for num,line in enumerate(lines):
            L = line.strip().split(";")
            if len(L)==9:
                try:
                    Product_id = int(L[0])
                    Product_name = str(L[1])
                    Product_category = str(L[2])
                    Price = int(L[3])
                    Inventory = int(L[4])
                    Supplier = str(L[5])
                    Has_on_offer = int(L[6])
                    Offer_price = int(L[7])
                    Valid_until = (datetime.strptime(L[8],'%m/%d/%Y')).date()

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
                except ValueError:
                    print(f"\033[2;91mValueError in \'products.txt\' file:There is invalid input value in line {num + 1},please check your text file and you can try again.\033[0m")

            else:
                print( f"\033[2;91mFormatError found in \'products.txt\' file:The number of features must be 7 in line {num + 1},please check your text file and you can try again.\033[0m")

    def addProduct(self):
        print("Please Fill The Information Of The Product :")
        try:
            Product_id=int(input("Enter Product_id:"))
            if self.isProductExist(self,Product_id):
                print(f"\033[2;91mThe product_id was found in products,please try again\033[0m")
                return
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
                Valid_until = (datetime.strptime(input("Enter Valid_until:"),'%m/%d/%Y')).date()
                print(type(Valid_until))
                print(Valid_until)
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
        except ValueError:
            print(f"\033[2;91mValueError:please enter a valid values\033[0m")
            return False
        return True

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
            try:
                choice = int(input("Enter your choice:\033[0m"))
            except ValueError:
                print(f"\033[2;91mInvalid value of choice,please try again\033[0m")
                continue
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
                case _:
                    print("\033[2;91mThere is no option in this number!!,please try again\033[0m")

    def saleOfProduct(self,product):
        try :
            product.Offer_price = int(input("Enter Offer_price:"))
            product.Valid_until = (datetime.strptime(input("Enter Valid_until:"), '%m/%d/%Y')).date()
            product.Has_on_offer = 1
        except ValueError:
            print(f"\033[2;91mInvalid value,please try again\033[0m")
            return
        print("\033[2;92mThe discount has been added to the product successfully\033[0m")

    def isProductExist(self,product_id):
        for product in self.products:
            if product.Id == product_id:
                return product
        return None

    def updateProduct(self,product):
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
                    try :
                        product.Name= input("Enter Name:")
                    except ValueError:
                        print(f"\033[2;91mInvalid value of name,please try again\033[0m")
                        continue
                case 2:
                    try:
                        product.Category = input("Enter Category:")
                    except ValueError:
                        print(f"\033[2;91mInvalid value of category,please try again\033[0m")
                        continue
                case 3:
                    try:
                        product.Price = int(input("Enter Price:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of price,please try again\033[0m")
                        continue
                case 4:
                    try:
                        product.Inventory = int(input("Enter Inventory:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of inventory,please try again\033[0m")
                        continue
                case 5:
                    try:
                        product.Supplier = input("Enter Supplier:")
                    except ValueError:
                        print(f"\033[2;91mInvalid value of supplier,please try again\033[0m")
                        continue
                case 6:
                    try:
                        product.Has_on_offer = int(input("Enter Has_on_offer:"))
                    except ValueError:
                        print(f"\033[2;91mInvalid value of has_on_offer,please try again\033[0m")
                        continue
                case 7:
                    if product.Has_on_offer:
                        try :
                            product.Offer_price = int(input("Enter Offer_price:"))
                            continue
                        except ValueError:
                            print(f"\033[2;91mInvalid value of offer_price,please try again\033[0m")
                            continue
                    print("\033[2;91mYou can't update this feature until update \"Has_on_offer\" to 1\033[0m")

                case 8:
                    if product.Has_on_offer:
                        try:
                            product.Valid_until = (datetime.strptime(input("Enter Valid_until:"),'%m/%d/%Y')).date()
                            continue
                        except ValueError:
                            print(f"\033[2;91mInvalid value of valid_until,please try again\033[0m")
                            continue
                    print("\033[2;91mYou can't update this feature until update \"Has_on_offer\" to 1\033[0m")
                case 9:
                    return
                case _:
                    print("\033[2;91mThere is no option in this number!!,please try again\033[0m")

            print("\033[2;92mThe product has been updated successfully\033[0m")

    def displayProduct(self,product_id):
        product=self.isProductExist(self,product_id)
        if product:
            print(product,end="")
            return (product.Price - product.Offer_price)
        return None

    def deductItemsOfProduct(self, product_id,numItems):
        product = self.isProductExist(self, product_id)
        if product:
            product.Inventory-=numItems
            if product.Inventory<0:
                print("Note: The number of items requested is greater than what is available")
                product.Inventory=0
            return True
        return False

    def saveProductsToFile(self):
        fileName=input("Enter a file where you want to save the products data:")
        while not fileName.endswith(".txt"):
            fileName = input("\033[2;91mError!,Please enter a valid filename(.txt) :\033[0m")
        file = open(fileName, "w")
        for product in self.products:
            file.write(f"{product.Id};{product.Name};{product.Category};{product.Price};{product.Inventory};{product.Supplier};{product.Has_on_offer};{product.Offer_price};{product.Valid_until}")
            file.write("\n")
        print(f"\033[2;91mThe products data was saved successfully in the {fileName} file.\033[0m")