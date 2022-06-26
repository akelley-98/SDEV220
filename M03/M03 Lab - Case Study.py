class Vehicle:

    def __init__(self, type, year, make, model, doors, roof ):
        self.type = type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
            
    def getType(self):
        self.type = input('Please enter the vehicle type (car or truck): ')
        
    def getYear(self):
        self.year = input('Please enter the vehicle year: ')
        
    def getMake(self):
        self.make = input('Please enter the vehicle make: ')
        
    def getModel(self):
        self.model = input('Please enter the vehicle model: ')

    def getDoors(self):
        self.doors = input('Please enter the number doors: ')
        
    def getRoof(self):
        self.roof = input('Please enter the type of roof (solid or sun): ')  

#creates instance
selection1 = Vehicle('n','n','n','n','n','n')

Vehicle.getType(selection1)
Vehicle.getYear(selection1)
Vehicle.getMake(selection1)
Vehicle.getModel(selection1)
Vehicle.getDoors(selection1)
Vehicle.getRoof(selection1)

print(f'Your vehicle is a: {selection1.type}')
print(f'Your vehicle year is: {selection1.year}')
print(f'Your vehicle make is: {selection1.make}')
print(f'Your vehicle model is: {selection1.model}')
print(f'Your vehicle has {selection1.doors} doors')
print(f'Your vehicle has a {selection1.roof} roof')