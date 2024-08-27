class Items:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"Name:{self.name}\t Price:{self.price}"
class ShoppingCart():
    def __init__(self):
        self.items = []
    def add_item(self,item:Items):
        self.items.append(item)
    def remove_item(self,item:Items):
        self.items.remove(item)
    def cost_of_cart(self):
        total = 0
        for items in self.items:
            total += items.price
        return total
    
    
# cart1  = ShoppingCart()
# cart1.add_item({'name':'kurti','price':300})
# cart1.add_item({'name':'jeans','price':400})

# cart2 = ShoppingCart()
# cart2.add_item({'name':'kurti','price':400})
# cart2.add_item({'name':'jeans','price':1000})
# # # print(cart1.items)
# # print(cart1.cost_of_cart())
# for items in cart2.items:
#     print(f"Name:{items['name']}\t Price:{items['price']}")
# print('-'*50)
# print("Total :\t\t",cart2.cost_of_cart())
item1= Items('kurti',300)
item2= Items('Jeans',900)
cart3 =ShoppingCart()
cart3.add_item(item1)
cart3.add_item(item1)
print("Items added in cart3:",cart3.items)
for i in cart3.items:
    print(i)
print('-'*30)
print("Total Cost of cart3:",cart3.cost_of_cart())