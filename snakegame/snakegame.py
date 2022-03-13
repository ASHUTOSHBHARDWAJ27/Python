import pygame
import random
# colors
white=(255,255,255)
black=(150,150,200)
red=(255,0,0)
foodcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
pygame.init()

screen_width=460 
screen_height=600 

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

clock=pygame.time.Clock()
font = pygame.font.SysFont(None,50)

def textscreen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plotsnake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,223,223))
        # gameWindow.blit(home,(0,0))
        textscreen("WELCOME TO SNAKES",red,33,33)
        textscreen("PESS SPACE TO PLAY",red,33,66)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    foodcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    snakecolor=(0,0,0)
    exit_game=False
    game_over=False
    snake_x=150
    snake_y=150
    snake_size=20
    food_x=random.randint(100,screen_width-100)
    food_y=random.randint(100,screen_height-100)
    initvelocity=5
    velocity_x=0
    velocity_y=0
    score=0
    fps=30
    snk_list=[]
    snk_lenght=1
  
    while not exit_game:
        if game_over:
           
            gameWindow.fill(white)
           
            textscreen("GAME OVER",(255,55,55),5,5)
            textscreen("PESS ENTER TO PLAY",(125,255,255),5,55)
            textscreen("YOUR SCORE:"+str(score),(255,211,233),5,99)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:            
            for event in pygame.event.get():
                      
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=initvelocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-initvelocity
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=initvelocity
                        velocity_x=0
                    if event.key==pygame.K_UP:
                        velocity_y=-initvelocity
                        velocity_x=0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score += 10
                food_x=random.randint(100,screen_width-100)
                food_y=random.randint(100,screen_height-100)
                snakecolor=foodcolor
                foodcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                
                snk_lenght+=5
             
            gameWindow.fill(white)
         
            textscreen("SCORE :"+str(score),red,5,5)
       
            pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(gameWindow,foodcolor,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_lenght:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            plotsnake(gameWindow,snakecolor,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()    