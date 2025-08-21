class Person:  
    def __init__(self, name, age, Address):  
        self.name = name    
        self.age = age  
        self.Address = Address    
    def greet(self):  
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old. I live in " + self.Address + ".")
  
# Create a new instance of the Person class and assign it to the variable person1  
person1 = Person("Ayan", 25, "Patna")  
person1.greet()    


