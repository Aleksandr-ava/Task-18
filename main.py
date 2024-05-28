class Buiding:
    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = 'пятиэтажка'

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType


numberOfFloors = Buiding
buildingType = Buiding
print(numberOfFloors == buildingType)
