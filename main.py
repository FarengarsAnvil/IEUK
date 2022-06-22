import random
#For generating the 20 random Obstacles in Phase 2.

#Create a Grid Class to instantiate Grid objects which are an Array of rows x column forming a Matrix.
class Grid():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid =[]
        self.obstacleList = []
        self.availablePaths = []

    def makegrid(self, row, column):
        for i in range(row):
            for j in range(column):
                self.grid.append((i,j))

    #Method sets the starting position for the Delivery route, in this case that is (0,0) but in real world terms that is the Warehouse Depot.
    def setStart(self,x,y):
        start = (x,y)
        print("Starting point origin is:",start)

    #Method takes X, Y Co-ordinates and adds them to a tuple to be the deliveryPoint, in this case that is (9,9), but in real world terms that is Delivery address.
    def setDeliveryPoint(self,x,y):
        deliveryPoint = (x,y)
        print("Delivery point is:",deliveryPoint)

    #Method allows the addition of an Obstacle to the Grid. Method is called with random module to generate 20 more obstacles in Phase 2.
    def addObstacle(self, x, y):
        obstacle = (x,y)
        if obstacle == (0,0) or obstacle ==(9,9):
            pass
        #Obstacle will only be added to self.obstacleList if it does not equal start or delivery or an existing
        if obstacle !=(0,0) and obstacle != (9,9):
            if obstacle not in self.obstacleList:
                self.obstacleList.append(obstacle)

        self.obstacleList = list(set(self.obstacleList))

    #Method prints all the Obstacles that are currently on the 10x10 Grid.
    def displayObstacles(self):
        print("Current Obstacles:",self.obstacleList)
        print("Current Obstacle Count:",len(self.obstacleList))

    #Method creates a List of all the Non-obstacle grid co-ordinates and when called will Print it.
    def displayPath(self):
        self.availablePaths = [x for x in self.grid if x not in self.obstacleList]
        print("Available Path:",self.availablePaths)

    #Method responsible for Phase 2 Answer. Uses recursion in order to find the Path from Start to Delivery point...
    #Whilst navigating around the Random obstacles.
    def moving(self, start, deliveryPoint):
        global current
        pathList = []
        pathList.append(start)
        current= list(start)
        final = list(deliveryPoint)
        #Parse the tuples in self.availablePaths list as List items so that i can compare find if an adjacent horizontal, vertical or diagonal...
        # Exists in self.availablePaths that is not in self.obstacleList.
        for i in range(len(self.availablePaths)):
            self.availablePaths[i] = list(self.availablePaths[i])
        #currentIncX is the Adjacent co-ordinate to the Current position.
        currentIncX = [current[0] +1, current[1]]
        #currentIncY is the co-ordinate that it is one Y axis unit above current position.
        currentIncY = [current[0], current[1] + 1]
        #currentDiagonal is the Diagonal position vector [1,1] from the current Position.
        currentDiagonal = [current[0]+1, current[1] +1]
        for i in range(len(self.availablePaths)):
                #Recursion Base Case: If current = Delivery location break loop and end recursion.
                if current == [9,9]:
                    break

                elif self.availablePaths[i] == currentDiagonal:
                    pathList.append(self.availablePaths[i])
                    current=currentDiagonal
                    self.moving(current,deliveryPoint)

                elif self.availablePaths[i] == currentIncY:
                    pathList.append(self.availablePaths[i])
                    current=currentIncY
                    self.moving(current,deliveryPoint)

                elif self.availablePaths[i] == currentIncX:
                    pathList.append(self.availablePaths[i])
                    current=currentIncX
                    self.moving(current,deliveryPoint)

        #Converts the co-ordinates from being list items back into Tuples.
        for i in range(len(pathList)):
            pathList[i] = tuple(pathList[i])

        solution =[]
        solution.append(pathList[0])
        print(solution)





    #Given that the Diagonal has no obstacles for Phase 1, this move func will just go up the Diagonal to delivery point (9,9).
    def move(self,start, deliveryPoint):
        counter = 0
        pathList = []
        startPos = list(start)
        delivery = list(deliveryPoint)
        while startPos[0] != delivery[0]:
           startPos[0] = startPos[0] +1
           startPos[1] = startPos[1] + 1
           counter = counter +1
           pathList.append(tuple(startPos))

        return pathList, counter






newGrid = Grid(10,10)
newGrid.makegrid(10,10)
newGrid.setStart(0,0)
newGrid.setDeliveryPoint(9,9)
newGrid.addObstacle(9,7)
newGrid.addObstacle(8,7)
newGrid.addObstacle(6,7)
newGrid.addObstacle(6,8)


print(newGrid.move((0,0),(9,9)))
#End of Phase 1



#Start Phase 2



while len(newGrid.obstacleList) != 24:
    newGrid.addObstacle(random.randrange(0,9),random.randrange(0,9))

newGrid.displayObstacles()
newGrid.displayPath()

newGrid.moving((0,0),(9,9))

#End of Phase 2. These are all the methods that are required for Phase 2 for solving the problem.




#By Muhammed Khidr
