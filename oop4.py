from abc import ABC

class animal(ABC):
    def move(self):
        pass
 
class snake(animal):
    def move(self):
        print("i slither")    
        
class human(animal):
    def move(self):
        print("i can run and crawl")   
        
        
class lion(animal):
    def move(self):
        print("i can roar")     

class frog(animal):
    def move(self):
        print("i can jump")


s = snake()
s.move()
h=human()
h.move()
l=lion()
l.move()
f=frog()
f.move()
                                  