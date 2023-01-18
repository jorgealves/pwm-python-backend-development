from dataclasses import dataclass

@dataclass
class Employee:
    name: str 
    age: int
    salary: float
    workplace: str

    def __str__(self) -> str:
        return f'Hi {self.name}, you´re {self.age}y, you are working at {self.workplace} earning {self.salary}.'


name = str(input("Your name: "))
age= int(input("Your age: "))
salary= float(input("Your salary expectation: "))
workplace= str(input("Your workplace: "))
result = Employee(name=name,age=age,salary=salary,workplace=workplace)
print(result)