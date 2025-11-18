class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
class DataEngineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.skills = ['Databricks', 'Python', 'SQL']
        
    def get_skill(self):
        return f"You have the following skills {self.skills}"
        
