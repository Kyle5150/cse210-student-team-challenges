import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

#Initializing the display window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Batter")

#Starting coordinates of the paddle
rect_x = 400
rect_y = 580

# #initial position of food
# food_x = 20
# food_y = 20

#initial speed of the paddle
rect_change_x = 0
rect_change_y = 0

#initial position of the ball
ball_x = 265
ball_y = 400

#speed of the ball
ball_change_x = 2
ball_change_y = 2

score = 0

#draws the paddle. Also restricts its movement between the edges
#of the window.
def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,RED,[x,y,100,20])

# def getPosFood(screen,x,y):
#     x = 20
#     y = 20
#     pos = x,y
#     return pos

food_x_list = []

food_y_list = []


def drawfoodrow1(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 40
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 40
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow2(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 76
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 76
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow3(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 112
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 112
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow4(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 148
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 148
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow5(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 184
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 184
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow6(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 220
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 220
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow7(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 256
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 256
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

def drawfoodrow8(x,y):
    # pos = getPosFood(screen, x, y)
    number_of_food = 20
    food_x = 40
    food_y = 292
    x = food_x
    y = food_y
    pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
    food_x_list.append(food_x)
    food_y_list.append(food_y)

    for n in range(number_of_food):
        food_x += 36
        food_y = 292
        pygame.draw.circle(screen, GREEN, (food_x, food_y), 12)
        food_x_list.append(food_x)
        food_y_list.append(food_y)

'''def drawball(screen,x,y):
    if x<0:
        x=0
        ball_change_x = ball_change_x * -1
    elif x>785:
        x=785
        ball_change_x = ball_change_x * -1
    elif y<0:
        y=0
        ball_change_y = ball_change_y * -1
    elif x>rect_x and x<rect_x+100 and y==565:
        ball_change_y = ball_change_y * -1
    elif y>600:
        ball_change_y = ball_change_y * -1                        
    pygame.draw.rect(screen,WHITE,[x,y,15,15])'''
    
#game's main loop    
done = False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -6
            elif event.key == pygame.K_RIGHT:
                rect_change_x = 6
            #elif event.key == pygame.K_UP:
                #rect_change_y = -6
            #elif event.key == pygame.K_DOWN:
                #rect_change_y = 6'''            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0            
    screen.fill(BLACK)
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    ball_x += ball_change_x
    ball_y += ball_change_y
    
    
    #this handles the movement of the ball.
    if ball_x < 0:
        ball_x = 0
        ball_change_x = ball_change_x * -1
    elif ball_x > 785:
        ball_x = 785
        ball_change_x = ball_change_x * -1
    elif ball_y < 0:
        ball_y = 0
        ball_change_y = ball_change_y * -1
    elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
        ball_change_y = ball_change_y * -1
    elif ball_x in food_x_list or ball_y in food_y_list:
        ball_change_y = ball_change_x * -1
        score = score + 1
    elif ball_y > 600:
        ball_change_y = ball_change_y * -1
        score = 0
        # pygame.quit()                
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,15,15])
    
    #drawball(screen,ball_x,ball_y)
    drawrect(screen,rect_x,rect_y)

    #draw food
    drawfoodrow1(40, 40)

    drawfoodrow2(40, 76)

    drawfoodrow3(40, 112)

    drawfoodrow4(40, 148)

    drawfoodrow5(40, 184)

    drawfoodrow6(40, 220)

    drawfoodrow7(40, 256)

    drawfoodrow8(40, 292)
    
    #score board
    font= pygame.font.SysFont('Calibri', 15, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text,[700,560])    
       
    pygame.display.flip()         
    clock.tick(60)
    
pygame.quit()    