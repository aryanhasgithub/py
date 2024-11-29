class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")




class employee(person):
    def __init__(self, name, age,salary,id):
        self.salary = salary
        self.id = id
        super().__init__(name, age)
     
        
per1 = employee("Arun Srivastav",34,12000,123456)   
per1.display()
print(per1.salary,per1.id)     
            