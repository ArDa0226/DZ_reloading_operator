
class Building:

    def __init__(self, buildingType, numberOfFloors):

        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
       return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building('Панельный', 1)
your_building = Building('Панельный', 1)
if my_building == your_building:
    print('Похожи...')
else:
    print('Не похожи...')


my_building_2 = Building('Деревянный', 1)
yuor_building_2 = Building('Шалаш', 1)
if my_building_2 == yuor_building_2:
    print('Похожи...')
else:
    print('Не похожи...')
