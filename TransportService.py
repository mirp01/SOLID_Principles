from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def startMoving():
        pass
    
    @abstractmethod
    def stopMoving():
        pass
    
class TransportService(ABC):
    def __init__(self, vehicles):
        self.vehicles = vehicles
    
    def assignVehicle(self, vehicleID):
        print(f"Vehicle with ID: {vehicleID} has been assigned a trip.")
        
    def startRide(self, vehicleID):
        print(f"Vehicle with ID: {vehicleID} started moving towards destination.")
        
    def endRide(self, vehicleID):
        print(f"Vehicle with ID: {vehicleID} arrived to the destination.")

class Truck(Vehicle):
    def __init__(self, id, model, fuel):
        self.id = id
        self.model = model
        self.fuel = fuel
    
    def startMoving(self):
        print("Truck driver started driving.")
        
    def stopMoving(self):
        print("Truck driver stopped the engine.")
        
    def refuel(self):
        print("Truck is refueling.")
        
class Bicycle(Vehicle):
    def __init__(self, id, model):
        self.id = id
        self.model = model
    
    def startMoving(self):
        print("Cyclist started pedaling.")
        
    def stopMoving(self):
        print("Cyclist stopped pedaling.")
        
    def rest(self):
        print("Cyclist is resting.")
        
def main():
    
    truck1 = Truck(1, "ELF-350", True)
    bicycle1 = Bicycle(2, "X-009")
    
    vehicles = [truck1, bicycle1]
    CheapRides = TransportService(vehicles)
    
    CheapRides.assignVehicle(1)
    CheapRides.startRide(1)
    CheapRides.endRide(1)
    truck1.refuel()
    
    
    pass

main()
    
        