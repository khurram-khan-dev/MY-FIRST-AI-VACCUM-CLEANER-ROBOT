import random

class vaccum:
    def __init__(self):
        self.build = [[''], [''], ['']]
        self.buildingfloor = [0, 1, 2]
        self.currentfloor = 0
        self.clean = 9

    def create_building(self):
        # creating rooms and floors

        self.build = [[0 for i in range(3)] for j in range(3)]
        return self.build

    def dirt(self):
        # placing dirt into rooms randomly

        for i in range(3):
            for j in range(3):
                n = random.randint(0, 1)
                self.build[i][j] = n

        return self.build

    def suck(self, floor, room):
        # sucking process

        # if all room will be clean
        if self.clean == 0:
            print("ALL DONE")

        # if not then cleaning of room start...
        else:

            # if all room is not clean on current floor
            if len(self.buildingfloor) != 0:

                if self.build[floor][room] == 1:
                    self.build[floor][room] = 0
                    self.buildingfloor.remove(room)
                    print("room remain on floor number:", floor , self.buildingfloor)
                    print("current", self.build, "\n")
                    b1.suck(floor, b1.moveroom())
                else:
                    # if current room is clean
                    if room in self.buildingfloor:
                        self.buildingfloor.remove(room)
                        b1.suck(floor, b1.moveroom())
                    else:
                        # move to next floor
                        b1.movefloor()

            # when all room on floor is cleaned
            else:
                self.clean -= 3
                self.buildingfloor = [0, 1, 2]
                if self.clean == 0:
                    pass
                else:
                    print("ROOM REMAINING TO CHECK FOR CLEANING ON FLOOR # ",floor+1, self.buildingfloor, "\n")
                    b1.movefloor
                    b1.suck(self.currentfloor, b1.moveroom())

            self.currentfloor = floor
            return self.build

    def moveroom(self):
        # moving room randomly on floor
        if len(self.buildingfloor) != 0:
            return random.choice(self.buildingfloor)
        else:
            # if all room is clean on floor then change room
            b1.movefloor()

    def movefloor(self):
        # moving floor
        #print('MOVING FLOOR ')
        print("ALL ROOM CLEANED ON FLOOR #", self.currentfloor, "moving to next floor \n")
        self.currentfloor += 1


# RUNNING THE MAIN CODE
while True:
    b1 = vaccum()
    b1.create_building()
    print("this is empty building \n", b1.build ,"\n")

    b1.dirt()
    print("this is after dirt \n", b1.build, "\n")

    print("which room you want to clean first: (0,1,2)")
    room = input()
    room = int(room)

    # cleaning start after deciding the room
    b1.suck(0, room)

    print("BUILDING AFTER CLEANING: \n", b1.build)
    print("ALL ROOM ON ALL FLOOR CLEANED!! GOALLL ACHEIVEDD!!!!")
    break



