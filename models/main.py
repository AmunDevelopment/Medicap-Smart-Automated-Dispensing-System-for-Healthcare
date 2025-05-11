from patient import Patient
from staff import Staff
from medicine import Medicine
from inventory import Inventory
from prescription import Prescription

'''
p1 = Patient(
    "Hossam",
    "1-1-2001",
    'M',
    '010101010',
    "Diabeters"
)
p1.uploadDatabase()


n1 = Staff(
    'sons',
    '2-2-2002',
    'F',
    '01010101010',
    'hii.txt',
    'Nurse'
)
n1.uploadDatabase()


m1 = Medicine(
    1,
    "drug1",
    "drug",
    "Tablet",
    5,
    "2-2-2030"
)
m1.uploadDatabase()

m2 = Medicine(
    1,
    "drug2",
    "drug",
    "Tablet",
    15,
    "2-2-2030"
)
m2.uploadDatabase()
'''
p1 = Prescription(
    'sons',
    'Hossam',
    'drug1',
    'gay',
    5,
    '10 times a week',
    '2-2-2070'
)
p1.uploadDatabase()