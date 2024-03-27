
class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)


    def __eq__(self, other):
       return self.numberOfFloors == other.buildingType


my_building = Building(1, 1)
if my_building.buildingType == my_building.numberOfFloors:
    print('Мы похожи...')
else:
    print('Не похожи...')