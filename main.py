# Connect 4 Game
import pygame

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
purple = (255, 0, 255)

# game window
windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Connect 4 - Multiplier Game")

rectWidth = 20
rectHeight = rectWidth
rectDict = {}
clickedRectDict = {}
count = 0
c_rectCount = 0
x1 = 0
y1 = 0
found = False
isEqual_X = False
isEqual_Y = False

# creating 144 rect dictionary
for x in range(rectWidth, windowWidth - rectWidth, rectWidth * 2):
    for y in range(rectHeight, windowHeight - rectHeight, rectHeight * 2):
        count += 1
        rectDict[f'rect_{count}'] = pygame.Rect(x, y, rectWidth, rectHeight)


# drawing rectangle's as circle
def drawCircle():
    for i in range(0, 144):
        pygame.draw.rect(window, black, rectDict[f'rect_{i + 1}'], border_radius=100)


# checking collisions between mouse and rect
def checkCollision():
    global x1, y1, c_rectCount, found
    if pygame.mouse.get_pressed(3)[0]:
        found = False
        x1, y1 = pygame.mouse.get_pos()
        for rectNum in range(0, 144):
            if rectDict[f'rect_{rectNum + 1}'].collidepoint(x1, y1):
                if c_rectCount == 0:
                    found = True
                    c_rectCount += 1
                    clickedRectDict[f'c_rect_{c_rectCount}'] = rectDict[f'rect_{rectNum + 1}']
                else:
                    for checkCount in range(0, c_rectCount):
                        if clickedRectDict[f'c_rect_{checkCount + 1}'] == rectDict[f'rect_{rectNum + 1}']:
                            found = True
                            break

                if not found:
                    c_rectCount += 1
                    clickedRectDict[f'c_rect_{c_rectCount}'] = rectDict[f'rect_{rectNum + 1}']
                    print(clickedRectDict)


# draw clicked circle
def drawClickedCircle(color):
    for c_rectNum in range(0, c_rectCount):
        pygame.draw.rect(window, color, clickedRectDict[f'c_rect_{c_rectNum + 1}'], border_radius=100)


# check if 4 dots are aligned or not
def checkWin():
    global isEqual_X, isEqual_Y
    for a1 in range(0, c_rectCount - 3):
        for a2 in range(a1 + 1, c_rectCount - 2):
            for a3 in range(a2 + 1, c_rectCount - 1):
                for a4 in range(a3 + 1, c_rectCount - 0):
                    if (clickedRectDict[f'c_rect_{a1 + 1}'].x == clickedRectDict[f'c_rect_{a2 + 1}'].x) and (clickedRectDict[f'c_rect_{a2 + 1}'].x == clickedRectDict[f'c_rect_{a3 + 1}'].x) and \
                            (clickedRectDict[f'c_rect_{a3 + 1}'].x == clickedRectDict[f'c_rect_{a4 + 1}'].x) and (clickedRectDict[f'c_rect_{a1 + 1}'].x == clickedRectDict[f'c_rect_{a3 + 1}'].x) and \
                            (clickedRectDict[f'c_rect_{a1 + 1}'].x == clickedRectDict[f'c_rect_{a4 + 1}'].x) and (clickedRectDict[f'c_rect_{a2 + 1}'].x == clickedRectDict[f'c_rect_{a4 + 1}'].x):
                        isEqual_X = True
                    elif (clickedRectDict[f'c_rect_{a1 + 1}'].y == clickedRectDict[f'c_rect_{a2 + 1}'].y) and (clickedRectDict[f'c_rect_{a2 + 1}'].y == clickedRectDict[f'c_rect_{a3 + 1}'].y) and \
                            (clickedRectDict[f'c_rect_{a3 + 1}'].y == clickedRectDict[f'c_rect_{a4 + 1}'].y) and (clickedRectDict[f'c_rect_{a1 + 1}'].y == clickedRectDict[f'c_rect_{a3 + 1}'].y) and \
                            (clickedRectDict[f'c_rect_{a1 + 1}'].y == clickedRectDict[f'c_rect_{a4 + 1}'].y) and (clickedRectDict[f'c_rect_{a2 + 1}'].y == clickedRectDict[f'c_rect_{a4 + 1}'].y):
                        isEqual_Y = True

    if isEqual_X:
        print("You won along x-direction")
    elif isEqual_Y:
        print("You won along y-direction")


# main function
def reDrawGameWindow():
    window.fill(blue)
    drawCircle()
    checkCollision()
    drawClickedCircle(green)
    checkWin()


# main game loop
def mainLoop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                run = False

        reDrawGameWindow()
        pygame.display.update()
    pygame.quit()


mainLoop()
