from src.models.person import Person
from src.models.database import Database
import os
class Staff(Person):
    facesID_path = os.path.join('src','data','known_faces')
    def __init__(self, name, birthDate, gender, contact,faceID,role):
        super().__init__(name, birthDate, gender, contact)
        self.faceID = faceID
        self.role = role
    def __ifExisits(self):
        target_img = os.path.join(self.facesID_path,self.faceID)
        if os.path.exists(target_img):
            return True
        return False
    def uploadDatabase(self):
        if not (self.__ifExisits()):
            #TODO: do more functionality
            raise Exception("Sorry , faceID doesnt exist.")
        db = Database()
        db.cursor.execute("INSERT INTO Staff (name,gender,contact,role,birth_date,face_id) VALUES(?,?,?,?,?,?)",
                          (self.name,self.gender,self.contact,self.role,self.birthDate,os.path.join(self.facesID_path,self.faceID)))
        db.connect.commit()
        