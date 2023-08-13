import pandas as pd
from Product import Product

#Assuming already have data into excel file into a dataframe df
df = pd.read_excel('Reading.xlsx', sheet_name='products')
print("%-20s%-20s%-10s" %("Product Name" , "Category" , "Price"))
print("-"*50)
pList = []

for index, row in df.iterrows():
    productName = row['pName']
    category = row['Category']
    price = row['Price']
    
    currentProduct = Product(productName,category,price)
    pList.append(currentProduct)
#print(currentProduct) ---> will display with name
#print(currentProduct.descrip())
    currentProduct.discount(5)
#print ("after:",currentProduct.descrip())
    
#Outside the loop
#print(len(pList))
for product in pList:
    #print (product.descrip())
    print("%-20s%-20s%-10.2f" %(product.getName(),product.getCategory(),product.getPrice()))

#20 for name ,
#20 for category ,
#10 for price ,
#f for the float

# Will not use descrip because it will give me not as table 
    #print (productName , " " , category, " ", price)