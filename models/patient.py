from src.models.person import Person
from src.models.database import Database
class Patient(Person):
    def __init__(self,name,birthDate,gender,contact,medicalHisotry):
        super().__init__(name,birthDate,gender,contact)
        self.medicalHistory = medicalHisotry
    def uploadDatabase(self):
        db = Database()
        db.cursor.execute("INSERT INTO Patient (name,gender,contact,medical_history,birth_date) VALUES(?,?,?,?,?)",
                         (self.name,self.gender,self.contact,self.medicalHistory,self.birthDate))
        db.connect.commit()