from src.models.database import Database
from abc import ABC, abstractmethod
from datetime import datetime
import serial.tools.list_ports
class Inventory(ABC):
    db = Database()
    drawerSymbol = None
    slotSymbol = None
    threshold = 10 #The least amout of medicine that can be in the inventory
    inventoryStock = 0 
    status = 0 #Drawer status 1-opened 0-closed
    drawer_open_time = 0
    drawer_close_time = 0
    def __init__(self,drawerNumber,drawerSlot):
        self.drawerNumber = drawerNumber
        self.drawerSlot = drawerSlot
        self.db.cursor.execute("SELECT current_stock FROM Inventory WHERE drawer_number=? AND drawer_slot=?",(self.drawerNumber,self.drawerSlot,))
        self.inventoryStock = self.db.cursor.fetchone()[0]
    def __checkThreshold(self):
        if self.inventoryStock <= self.threshold:
            print("Low on medicine")
            #TODO: do something
    
    def _updateInventoryStock(self,quantity):
        self.db.cursor.execute("UPDATE Inventory SET current_stock=? WHERE drawer_number=? AND drawer_slot=?",(self.inventoryStock-quantity,self.drawerNumber,self.drawerSlot))
        self.__checkThreshold()

    def openDrawer(self,port):
        if(self.drawerNumber == 1):
            self.drawerSymbol = 'A'
        elif(self.drawerNumber == 2):
            self.drawerSymbol = 'B'
        self.slotSymbol = str(self.drawerSlot-1)
        message ='open'+self.slotSymbol+self.drawerSymbol
        port.write(message.encode('utf-8'))
        self.drawer_open_time = datetime.now()

    def closeDrawer(self,port,staffID,medicineID,quantity,patient):
        message ='close'+self.slotSymbol+self.drawerSymbol
        port.write(message.encode('utf-8'))
        self.drawer_close_time = datetime.now()
        self.__Upload_log(staffID,medicineID,quantity,patient)
    
    def __Upload_log(self,staffID,medicineID,quantity,patient):
        self.db.cursor.execute(
            "INSERT INTO Log (drawer_number,drawer_slot,staff_id,medicine_id,quantity,opened_date,closed_date,patient_name) VALUES(?,?,?,?,?,?,?,?)",
            (self.drawerNumber,self.drawerSlot,staffID,medicineID,quantity,self.drawer_open_time,self.drawer_close_time,patient)
        )
        self.db.connect.commit()

    @abstractmethod
    def uploadDatabase():
        #TODO: update database.
        pass


        