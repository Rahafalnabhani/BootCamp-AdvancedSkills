#Create product class ,
#each product has name , category and price ---->instance variable
#class is able to return a discription of product --> method
#each product be able to compute discount of given amount
# Compute price after discount of amount%


class Product():
    def __init__(self,name,category,price):
        self.name = name
        self.category=category
        self.price=price
        
       #We can't update or change 
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price
    
     #We can update or change
    def set_name(self,newName):
            self.name = newName
    def set_category(self,newCategory):
            self.category = newCategory
    def set_price(self,newPrice):
            self.price = newPrice
    
    
    def descrip(self):
            return f"The Product: {self.name}, {self.category} , {self.price}"
        
    # It can be updated 
    #def discout(self,amount):
        #result= self.price - (self.price * amount/100)
        
   # The price updated by the discount
    def discount(self,amount):
        self.price= self.price - (self.price * amount/100)
        if  self.category == "Electroics":
            self.price +=10
    