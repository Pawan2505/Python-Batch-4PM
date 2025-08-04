
# type(obj)	Returns the type/class of object
# id(obj)	Returns memory address of object
# hasattr()	Checks if object has that attribute
# getattr()	Gets the value of an attribute
# setattr()	Sets or updates the attribute value
# delattr()	Deletes an attribute

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name :",self.name)
        print("Age :",self.age)
        
class Child(Student):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.num = num
    def show(self):
        super().show()
        print("Num :",self.num)
    
s = Student('Pawan',22)
c = Child("Manish",23,34)

# s.show()
c.show()

# print(type(s))
# print(type(c))