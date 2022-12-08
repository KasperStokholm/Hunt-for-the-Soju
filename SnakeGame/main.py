import pygame
import random
import sys

pygame.init()

# Set the screen size
SCREEN_SIZE = (500, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)

image_jan = pygame.image.load(r'C:\Users\Kasper\Pictures\Jan.jpg').convert()
image_soju = pygame.image.load(r'C:\Users\Kasper\Pictures\Soju.png').convert()
image_cu = pygame.image.load(r'C:\Users\Kasper\Pictures\CU.png').convert()


# Set the title of the window
pygame.display.set_caption('Snake')

# Set the initial position and size of the snake
x = 250
y = 250
snake_block = 40

food_x = round((random.randint(0, SCREEN_SIZE[0]))/10)*10
food_y = round((random.randint(0, SCREEN_SIZE[1]))/10)*10
#print(f"Food position: {food_x} : {food_y}")
#print(f"Snake position: {x} : {y}")

direction = 'RIGHT'

score = 0

speed = 15
color = (255, 0, 0)

# Set the initial font of the text
font = pygame.font.SysFont('comicsansms', 24)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])

        screen.blit(image_jan, (x[0], x[1]))

# Function to display the score
def show_score(x, y, score):
    score_text = font.render(f'Score: {score}', True, (255, 0, 0))
    screen.blit(score_text, (x, y))


# Function to check if the snake has collided with the food
def check_food_collision(x, y, food_x, food_y):
    if food_x-10 <= x <= food_x+10 and food_y-10 <= y <= food_y+10:
        return True
    return False


# Function to check if the snake has collided with the wall or itself
def check_collision(x, y, length):
    if x < 0 or x >= SCREEN_SIZE[0] or y < 0 or y >= SCREEN_SIZE[1]:
        return True
    return False


# Game loop
while True:
    # Fill the screen with black color

    screen.blit(image_cu, (0, 0))

    # Set the initial length of the snake
    length = 1

    snake_List = []
    x_change = 0
    y_change = 0

    # Loop through all the events
    for event in pygame.event.get():
        # Check if the user has quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if the user has pressed any key
        if event.type == pygame.KEYDOWN:
            # Check if the user has pressed the left arrow key
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            # Check if the user has pressed the right arrow key
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            # Check if the user has pressed the up arrow key
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            # Check if the user has pressed the down arrow key
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # Update the position of the snake based on the direction
    if direction == 'RIGHT':
        x_change = 10
        y_change = 0
    elif direction == 'LEFT':
        x_change = -10
        y_change = 0
    elif direction == 'UP':
        y_change = -10
        x_change = 0
    elif direction == 'DOWN':
        y_change = 10
        x_change = 0

    # Check if the snake has collided with the wall or itself
    if check_collision(x, y, length):
        break

    # Check if the snake has collided with the food
    if check_food_collision(x, y, food_x, food_y):
        # Generate a new food item at a random position
        food_x = round((random.randint(0, SCREEN_SIZE[0] - 40))/10)*10
        food_y = round((random.randint(0, SCREEN_SIZE[1] - 40))/10)*10

        # Increase the length of the snake - NOT WORKING FOR SOME REASON
        length = length + 1

        # Increase the score
        score += 1

        # Increase the speed of the game
        speed += 2

        # Change the color of the snake
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    x += x_change
    y += y_change

    #Drawing the snake parts - NOT CURRENTLY WORKING
    snake_Head = [x, y]
    snake_List.append(snake_Head)
    if len(snake_List) > length:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    our_snake(snake_block, snake_List)

    # Draw the food on the screen
    pygame.draw.rect(screen, (255, 255, 255), (food_x, food_y, snake_block, snake_block))
    screen.blit(image_soju, (food_x, food_y))

    # Display the score on the screen
    show_score(5, 5, score)

    # Update the screen
    pygame.display.update()

    # Set the frame rate of the game
    pygame.time.Clock().tick(speed)
