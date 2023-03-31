import queue
import turtle
import numpy as np
import random
from turtle import *
from queue import PriorityQueue as PQueue

sc = turtle.Screen()
point = turtle.Turtle()


class White(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("black","white")   
        self.shapesize(1.5, 1.5, 1)         
        self.penup()                    
        self.speed(0)

class Gray(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","gray")
        self.shapesize(1.5, 1.5, 1)  
        self.penup()
        self.speed(0)
        
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","red")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)
        
class Fuchsia(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","fuchsia")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)

class Olive(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","olive")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","green")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)
        
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","blue")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)

class Purple(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","purple")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)

class Pink(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","pink")
        self.shapesize(1.5, 1.5, 1)
        self.penup()
        self.speed(0)
        
def readfile():
    file = open('input.txt','r')
    data = file.read()
    listData = data.split('\n')
    return listData

def drawNumber(x, y, number):
    turtle.penup()
    turtle.goto(-325 + (x * 30), -260 + (y * 30))
    turtle.pendown()
    size = 12
    kind =('Arial', size)
    turtle.write(number, font = kind)
    turtle.ht()

def drawLetter(x,y,letter):
    turtle.penup()
    turtle.goto(-325 + (x * 30), -260  + (y * 30))
    turtle.pendown()
    turtle.color("black")
    size = 12
    kind = ('Arial', size)
    turtle.write(letter, font = kind)
    turtle.ht()

def createMatrix():
    global width ,height, matrix
 
    size = data[0].split(' ')
    width = int(size[0]) + 1
    height = int(size[1]) + 1
    matrix = np.zeros([height, width], dtype = int) #Create array of zero

    for i in range(height):
        for j in range(width):
            if (j == width-1 or (i == height-1 ) or j == 0 or i == 0):
                matrix[i][j] = 1
    

def drawmatrix(white, gray):
    createMatrix()
    speed(0.1)
    for y in range(height):
        for x in range(width):
            character = matrix[y][x]
            Posm = -320 + (x * 30)
            Posn = -250  + (y * 30)
            if character == 0:
                white.goto(Posm, Posn)
                white.stamp()
            if character == 1:
                gray.goto(Posm, Posn)
                gray.stamp()
                
    for y in range(height):
        drawNumber(-1, y, y)    
    for x in range(width):
        drawNumber(x, -1, x) 
        
def drawPosition(x, y, color):
    Posm = -320 + (x * 30)
    Posn = -250  + (y * 30)
    color.penup()
    color.goto(Posm, Posn)
    color.stamp()  
    color.pendown()
    color.speed(0)

def drawBeginAndGoal():
    speed(0)
    global begin, goal, beginX, beginY, goalX, goalY 

    temp = data[1].split(' ')
    beginX = int(temp[0])
    beginY = int(temp[1])
    goalX = int(temp[2])
    goalY = int(temp[3])

    begin = [beginX, beginY]
    goal = [goalX, goalY]

    matrix[beginY][beginX] = 1
    matrix[goalY][goalX] = 0

    drawPosition(beginX, beginY, blue)
    drawLetter(beginX, beginY, "S")
    
    drawPosition(goalX, goalY, blue)
    drawLetter(goalX, goalY, "G")

def drawEdge(pos1 ,pos2 ,color):
    speed(0)
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    
    a = y1 - y2
    b = x2 - x1
    c = a * x1 + b * y1
    
    matrix[y1][x1] = 2
    matrix[y2][x2] = 2
    if x1 == x2:
        if y1 < y2:
            for y1 in range(y1 + 1, y2):
                drawPosition(x1, y1, color)
                matrix[y1][x1] = 2
        else:
            for y2 in range(y2 + 1, y1):
                drawPosition(x1, y2, color)
                matrix[y2][x1] = 2
    if y1 == y2:
        if x1 < x2:
            for x1 in range(x1 + 1, x2):
                drawPosition(x1, y1, color)
                matrix[y1][x1] = 2
        else:
             for x2 in range(x2 + 1, x1):
                drawPosition(x2, y1, color)
                matrix[y1][x2] = 2
    if abs(a) > abs(b):
        if y1 < y2:
            for y1 in range(y1 + 1, y2):
                x = (c - b*y1) // a
                drawPosition(x,y1,color)
                matrix[y1][x] = 2
        else:
            for y2 in range(y2 + 1, y1):
                x = (c - b * y2) // a
                drawPosition(x, y2, color)
                matrix[y2][x] = 2
    else:
        if x1 < x2:
            for x1 in range(x1 + 1, x2):
                y = (c - a * x1) // b
                drawPosition(x1, y, color)
                matrix[y][x1] = 2
        else:
            for x2 in range(x2 + 1, x1):
                y = (c - a * y2) // b
                drawPosition(x2, y, color)
                matrix[y][x2] = 2
    
def drawObstacle():
    speed(0)
    numberOfObs = int(data[2])
    for i in range(3, numberOfObs + 3, 1):
        lst_vestices = []
        vestices = data[i].split(" ")
        clr = random.randint(0, len(listColor) - 1)
        
        for j in range(0, len(vestices), 2):
            posm = int(vestices[j])
            posn = int(vestices[j + 1])
            lst_vestices.append([posm, posn]) 
            drawPosition(posm, posn, listColor[clr])
        
        clr1 = random.randint(0, len(listColor) - 1)
        for k in range (len(lst_vestices)):
            if k == len(lst_vestices) - 1:
                drawEdge(lst_vestices[-1], lst_vestices[0], listColor[clr1])
            else:
                drawEdge(lst_vestices[k], lst_vestices[k + 1], listColor[clr1])
            


def BFS():
    speed(0)
    visited = []
    queue = []

    visited.append(begin)
    queue.append(begin)
    res[(beginX, beginY)] =  beginX, beginY

    while queue:
        cur = queue.pop(0)
        x = cur[0]
        y = cur[1]

        if [x, y] != begin: drawPosition(x,y,purple)

        if (matrix[y][x-1] == 0) and [x-1,y] not in visited:
            queue.append([x-1,y])
            visited.append([x-1,y])
            res[(x-1, y)] = x, y

        if (matrix[y][x+1] == 0) and [x+1,y] not in visited:
            queue.append([x+1,y])
            visited.append([x+1,y])
            res[(x+1, y)] = x, y

        if (matrix[y-1][x] == 0) and [x,y-1] not in visited:
            queue.append([x,y-1])
            visited.append([x,y-1])
            res[(x, y-1)] = x, y

        if (matrix[y+1][x] == 0) and [x,y+1] not in visited:
            queue.append([x,y+1])
            visited.append([x,y+1])
            res[(x, y+1)] = x, y
            
        if goal in visited:
            break

def UCS():
    speed(0)
    dis = np.zeros([width, width], dtype = int) #Create array of zero
    visited = []
    cost = 0
    max = 2
    
    visited.append(begin)

    q = PQueue()
    q.put((1,(beginX,beginY)))

    dis[beginX][beginY] = 0
    res[(beginX, beginY)] =  beginX, beginY

    while not q.empty():
        cur = q.get()
        cost = cur[0]
        cell = cur[1]
        x = cell[0]
        y = cell[1]
        i = 0
        if [x, y] != begin and [x, y] != goal: 
                drawPosition(x,y,purple)
                drawLetter(x,y,dis[x][y])
        
        count = 0
        for i in range (4):
            if (count == 4) : max+= cost

            if (matrix[y][x-1] == 0 ) and [x-1,y] not in visited:
                dis[x-1][y] = dis[x][y] + cost
                if(dis[x-1][y] < max):
                    q.put((cost,(x-1,y)))
                    visited.append([x-1,y])         
                    res[(x-1, y)] = x, y
                    i = 3
                else: count+=1
                
            if (matrix[y][x+1] == 0) and [x+1,y] not in visited:
                dis[x+1][y] = dis[x][y] + cost
                if(dis[x+1][y] <  max ):
                    q.put((cost,(x+1,y)))
                    visited.append([x+1,y])
                    res[(x+1, y)] = x, y
                    i = 3
                else: count+=1
                
            if (matrix[y-1][x] == 0) and [x,y-1] not in visited:
                dis[x][y-1] = dis[x][y] + cost
                if(dis[x][y-1] <  max):
                    q.put((cost,(x,y-1)))
                    visited.append([x,y-1])
                    res[(x, y-1)] = x, y
                    i = 3
                else: count+=1
                
            if (matrix[y+1][x] == 0) and [x,y+1] not in visited:
                dis[x][y+1] = dis[x][y] + cost
                if(dis[x][y+1] <  max):
                    q.put((cost,(x,y+1)))
                    visited.append([x,y+1])
                    res[(x, y+1)] = x, y
                    i = 3
                else: count+=1

        if goal in visited:
            break

def isValidDFS(x, y, visited, depth, limit):

    if depth > limit:
        return False

    if [x, y] == goal: 
        return True

    if [x, y] != begin: drawPosition(x, y, purple)


    visited.append([x, y])
    for i in range(4):
        m = x + col[i]
        n = y + row[i]
        if (matrix[n][m] == 0) and [m, n] not in visited:
            if (isValidDFS(m, n, visited,  depth + 1, limit) == True):
                res[(m, n)] = x, y
                return True

def IDS():

    foundGoal = False
    limit = 0
    x, y = beginX, beginY
    visited = []
    
    while not foundGoal:
        visited.clear()
        res.clear()
        
        limit += 1
        foundGoal = isValidDFS(x, y, visited, 0, limit)

def Manhattan(x1, y1, x2, y2):
    disMan = abs(x1 - x2) + abs(y1 - y2)
    return disMan

def addFrontier(frontier, listCost, value, array):
    for i in frontier:
        if (i == array and listCost[i[0], i[1]] > value):
            listCost[i[0], i[1]] = value
            return
    frontier.append(array)
    listCost[array[0], array[1]] =  value

def GBFS():
    speed(0)
    listCost = {}
    frontier = []
    visited = []
    
    frontier.append(begin)
    listCost[(beginX, beginY)] = 0
    res[(beginX, beginY)] =  beginX, beginY
    
    while goal not in visited:
        cur = frontier.pop(0)
        x = cur[0]
        y = cur[1]
    
        if ([x, y] != begin): drawPosition(x, y, purple)
        
        for i in range(4):
            m = x + col[i]
            n = y + row[i]
            if (matrix[n][m] == 0) and [m, n] not in visited:
                distance = Manhattan(m, n, goalX, goalY)
                addFrontier(frontier, listCost, distance, [m, n])
                visited.append([m, n])
                res[(m, n)] = x, y

def GSA():
    speed(0)
    listCost = {}
    frontier = []
    visited = []
    
    frontier.append(begin)
    listCost[(beginX, beginY)] = (1, 0)
    res[(beginX, beginY)] =  beginX, beginY
    
    while goal not in visited:
        cur = frontier.pop(0)
        x = cur[0]
        y = cur[1]
        (cost,cost) = listCost[x, y] 
        if ([x, y] != begin): drawPosition(x, y, purple)
        
        for i in range(4):
            m = x + col[i]
            n = y + row[i]
            if (matrix[n][m] == 0) and [m, n] not in visited:
                distance = Manhattan(m, n, goalX, goalY)
                addFrontier(frontier, listCost, (cost + distance + 1, cost + 1), [m, n])
                visited.append([m, n])
                res[(m, n)] = x, y


def backRouteBFS(x, y):
    cost = 0
    m = x
    n = y

    while(x, y) != (beginX, beginY):
        a, b = int(res[x, y][0]), int(res[x, y][1])
        if [x, y] != goal:drawPosition(x, y, pink)
        cost += 1
        x, y = int(a), int(b)

    count = cost

    while(m, n) != (beginX, beginY):
        c, d = int(res[m, n][0]), int(res[m, n][1])
        drawLetter(m, n, count)
        count -= 1
        m, n = int(c), int(d)

    message = 'Cost: ' + str(cost)
    penup()
    goto(0, -315)
    color("black")
    pendown()
    write(message, False, align= 'center',font= ('Arial', 15, 'bold'))

def backRoute(x, y):
    cost = 0

    while(x, y) != (beginX, beginY):
        a, b = int(res[x, y][0]), int(res[x, y][1])
        drawPosition(x, y, pink)
        cost += 1
        x, y = int(a), int(b)


    message = 'Cost: ' + str(cost)
    penup()
    goto(0, -315)
    color("black")
    pendown()
    write(message, False, align= 'center',font= ('Arial', 15, 'bold')) 

def menu():
    print("Choose: ")
    print("1. Breadth-first search")
    print("2. Uniform-cost search")
    print("3. Iterative deepening search")
    print("4. Greedy-best first search")
    print("5. Graph-search A*")
    print("0. Exit")

    choice = int(input("Input: "))

    drawmatrix(white,gray)
    drawBeginAndGoal()
    drawObstacle()

    if choice == 1:
        BFS()
        backRouteBFS(goalX,goalY)
    elif choice == 2: UCS()
    elif choice == 3: IDS()
    elif choice == 4: GBFS()
    elif choice == 5: GSA()

    if choice != 1: backRoute(goalX,goalY)


white = White()
gray = Gray()
red = Red()
fuchsia = Fuchsia()
olive = Olive()
green=Green()
blue = Blue()
purple = Purple()
pink = Pink()


listColor = [red, fuchsia, olive, green]
col = [1, 0 , -1, 0]
row = [0, 1, 0, -1]

data = readfile()
res = {}
menu()

sc.exitonclick()