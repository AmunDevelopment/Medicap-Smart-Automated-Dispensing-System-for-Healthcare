from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,birthDate,gender,contact):
        self.name = name
        self.birthDate = birthDate
        self.gender = gender
        self.contact = contact
    @abstractmethod
    def uploadDatabase():
        pass