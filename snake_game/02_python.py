import pygame
from numpy import random

x = pygame.init()

screen_width = 800
screen_height = 500
# game window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snake_list, snake_size):    
    
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# game loop
def gameloop():

    game_over = False
    exit_game = False
    snake_y = 55
    snake_x = 45
    food_x = random.randint(20, screen_width / 1 )
    food_y = random.randint(20, screen_height / 3 )
    snake_size = 10
    velocity_x = 0
    velocity_init = 5
    velocity_y = 0
    score = 0
    fps = 30
    snake_list = []
    snake_length = 1

    while not exit_game: 

        if game_over:
            gameWindow.fill((0, 0, 0))
            text_screen("Game Over ! Please Enter To Continue", (255, 0, 0), screen_width/6, screen_height/2)
            text_screen("Your Score: {}".format(score), (255, 0, 0), screen_width/6, screen_height/3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
    
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity_init
                        velocity_y = 0

                    elif event.key == pygame.K_LEFT:
                        velocity_x = -velocity_init
                        velocity_y = 0

                    elif event.key == pygame.K_UP:
                        velocity_y = -velocity_init
                        velocity_x = 0

                    elif event.key == pygame.K_DOWN:
                        velocity_y = velocity_init
                        velocity_x = 0            
            

            snake_x +=velocity_x
            snake_y +=velocity_y


            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score +=1 
                food_x = random.randint(20, screen_width / 1 )
                food_y = random.randint(20, screen_height / 3 )
                snake_length+=5


            gameWindow.fill((0, 0, 0))
            text_screen("Score {}".format(score), (255, 0, 0), 5 , 5)
            pygame.draw.rect(gameWindow, (255, 0, 0), [food_x, food_y, snake_size, snake_size]) 


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]


            if head in snake_list[:-1]:
                game_over = True    

            
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, (255, 255, 255), snake_list, snake_size)


        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
gameloop()    
