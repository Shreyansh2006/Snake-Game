import pygame
import random
import os


pygame.mixer.init()

pygame.init()



# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
lightpurple = (233, 220, 225)

# Creating window
screen_width = 850
screen_height = 650
gameWindow = pygame.display.set_mode((screen_width, screen_height))


# Background image
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
# Game Title
pygame.display.set_caption("#SnakesWithShreyansh")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# with open("hiscore.txt", "r"):


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 220, 225))
        text_screen("Hello Player,", blue, 320, 150)
        text_screen("Welcome To Snake", black, 270, 220)
        text_screen("Press Space Bar To Play", red, 230, 280)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('nagin.mp3')
                    pygame.mixer.music.play()
                    gameloop()



        pygame.display.update()
        clock.tick(25)


# Game Loop
def gameloop():


    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 430
    snake_y = 500
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # check if high Score file exist


    # with open("high Score.txt", "a") as f:
    #     f.append()
            
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width /2)
    food_y = random.randint(20, screen_height /2)
    score = 0
    init_velocity = 15
    snake_size = 25
    fps = 25

    while not exit_game:
        if game_over:
            # if (not os.path.exists("hiscore.txt")):
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
            text_screen("Score: " + str(score)+  "  High Score:"+str(hiscore), blue, 5, 5)
           
    



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('nagin.mp3')
                        pygame.mixer.music.play()

                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0





                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0



                    if event.key == pygame.K_q:
                        score +=10



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score)+ "  High Score:"+str(hiscore), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
# THANK YOU







