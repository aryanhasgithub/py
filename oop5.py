class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def sounds(self):
        print("bark")    
    
    def info(self):
        print(f"The dog's name is {self.name} and it is {self.age} years old.")
        
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def sounds(self):
        print("mew")    
    
    def info(self):
        print(f"The cat's name is {self.name} and it is {self.age} years old.")


cat1=cat('banny',2)   
dog1=dog('bunty',3)
for animal in (cat1, dog1):
    animal.sounds()
    animal.info()
    
                  
        
        