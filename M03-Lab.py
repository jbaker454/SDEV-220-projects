class Vehicle():
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type

class automobile(Vehicle):
    def __init__(self,vehicle_type,year,make,model,doors,roof):
        Vehicle.__init__(self,vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def get_user_information():
    vehicle_info = {}
    print("input your vehicle info here")
    vehicle_info["type"] = input("type: ")
    vehicle_info["year"] = input("year: ")
    vehicle_info["make"] = input("make: ")
    vehicle_info["model"] = input("model: ")
    vehicle_info["doors"] = input("door #: ")
    vehicle_info["roof"] = input("roof type: ")
    return vehicle_info

def print_user_info(user_vehicle):
    print("vehicle type:",user_vehicle.vehicle_type)
    print("year:",user_vehicle.year)
    print("make:",user_vehicle.make)
    print("model:",user_vehicle.model)
    print("door #:",user_vehicle.doors)
    print("roof:",user_vehicle.roof)

def main():
    vehicle_info = get_user_information()
    user_vehicle = automobile(
        vehicle_type = vehicle_info.get("type"),
        year = vehicle_info.get("year"),
        make = vehicle_info.get("make"),
        model = vehicle_info.get("model"),
        doors = vehicle_info.get("doors"),
        roof = vehicle_info.get("roof"),)
    print_user_info(user_vehicle)
    
main()
