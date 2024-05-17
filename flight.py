class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name)
        if not self.open_seats():
            return False
        self.passengers.append(name)
            return True


    def open_seats(self):
        return self.capacity - len(self.passengers)

# Call the class from above
flight = Flight(3)

people  = ["Harry", "Ron", "Hermoine", "Ginny"]
for person in people:
    
