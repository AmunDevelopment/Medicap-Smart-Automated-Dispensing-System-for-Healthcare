from src.models.inventory import Inventory
from src.models.database import Database
from datetime import datetime,date
class Medicine(Inventory):
    db = Database()
    def __init__(self, drawerNumber,drawerSlot,name,category,dosage_form,medicineStock,medicine_expiration_date):
        super().__init__(drawerNumber,drawerSlot)
        self.name = name
        self.category = category
        self.dosage_form = dosage_form
        self.medicineStock = medicineStock
        self.medicine_expiration_date = medicine_expiration_date
    def uploadDatabase(self):
        self.db.cursor.execute("INSERT INTO Medicine(drawer_number,drawer_slot,name,category,dosage_form,stock,expiration_date) VALUES (?,?,?,?,?,?,?)",
                          (self.drawerNumber,self.drawerSlot,self.name,self.category,self.dosage_form,self.medicineStock,self.medicine_expiration_date))
        self.db.connect.commit()
    
    def get_medicineID(self):
        result =self.db.cursor.execute("SELECT id FROM Medicine WHERE name=?",(self.name,))
        return result.fetchone()[0]
    @staticmethod
    def dispenseMedicine(medicine,quantity,staff):
        db = Database()
        medicine.medicineStock = medicine.medicineStock - quantity
        medicine._updateInventoryStock(quantity)
        db.cursor.execute("UPDATE Medicine SET stock=? WHERE name = ?",(medicine.medicineStock,medicine.name))
        db.connect.commit()
        #test
        print(f"staff: {staff} has dispensed: {str(medicine.name)} quntatiy: {medicine.medicineStock} \n the inventory is currently:{medicine.inventoryStock}")
        #TODO: update log
        pass
    @staticmethod
    def is_expired(dateEx):
        current_date = date.today()
        expire_date = datetime.strptime(dateEx,"%Y-%m-%d").date()
        if(current_date >= expire_date):
            return True