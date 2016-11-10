#create simple square dungeon with a player character that can move around inside of it.
import random
def createDungeon():
    dungeon = []
    for x in range(WIDTH): 
        dungeon.append([])
        for y in range(HEIGHT):
            # placeholder floor tile generation, replace eventually when i know what im doing :^)
            if random.randint(0,1) == 0:
                dungeon[x].append('~')
            else:
                dungeon[x].append('*')
    return dungeon

def getRow(dungeon, rowNum):
    row = ''
    for x in range(len(dungeon)):
        row += dungeon[x][rowNum]
    return row

def drawDungeon(dungeon):
    for y in range(HEIGHT):
        print(getRow(dungeon, y))

def drawWalls(dungeon):
    # draw side walls
    for x in range(WIDTH):
        if x == 0 or x == WIDTH - 1:
            for y in range(HEIGHT):
                dungeon[x][y] = '|'

    # draw top and bottom walls
    for y in range(HEIGHT):
        if y == 0 or y == HEIGHT - 1:
            for x in range(WIDTH):
                dungeon[x][y] = '#'

WIDTH = 37
HEIGHT = 25
dungeon = createDungeon()
drawWalls(dungeon)
drawDungeon(dungeon)
