class Person():
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        
    def __repr__(self):
        return f"{self.name} {self.lastname}"
    
    @classmethod
    def Person_fromstring(cls,string):
        return cls(string.split(" ")[0],string.split(" ")[1])
    
class Student(Person):
     def __init__(self, name,lastname,programme):
        super().__init__(name,lastname)
        self.programme = programme
    
     def __repr__(self):
        return super().__repr__() + f" {self.programme}"
