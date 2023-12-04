# Classes exercise

class Vehicle:
    def __init__(self, make, model, running = False):
        self.make = make
        self.model = model
        self.running = running
    def __str__(self):
        return f"Vehicle is {self.make} model {self.model}."
    def start(self):
        self.running = True
        print('running...')
    def stop(self):
        self.running = False
        print('stopped...')

car = Vehicle('Tesla', 'Model S')
print(car)
car.start()
car.stop()