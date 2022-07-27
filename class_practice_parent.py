class Cars():
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def disp_car(self):
        return f'Car: {self.make, self.model, self.color}'
