class price:
    def __init__(self):
        self.__price = 200
    
    
    def get_price(self):
        print("price: ", self.__price) 
    
    def change_price(self, price):
        self.__price = price
    
    
c = price()              
c.get_price()
c.__price = 225
c.get_price()
c.change_price(222)
c.get_price()
    