#!python
import pygame
import random
import sys

from config import config


def update_position(snake, direction, step):
    if direction == "UP":
        snake = [snake[0], snake[1] - step]
    if direction == "DOWN":
        snake = [snake[0], snake[1] + step]
    if direction == "LEFT":
        snake = [snake[0] - step, snake[1]]
    if direction == "RIGHT":
        snake = [snake[0] + step, snake[1]]
    return snake


def update_direction(direction, keys):
    if keys[pygame.K_LEFT]:
        return "LEFT" if direction != "RIGHT" else direction
    if keys[pygame.K_RIGHT]:
        return "RIGHT" if direction != "LEFT" else direction
    if keys[pygame.K_UP]:
        return "UP" if direction != "DOWN" else direction
    if keys[pygame.K_DOWN]:
        return "DOWN" if direction != "UP" else direction
    return direction


def is_out(snake, game_res):
    if snake[0] < 0 or snake[1] < 0 or snake[0] >= game_res[0] or snake[1] >= game_res[1]:
        return True
    return False


def game_over(window):

    print("GAME OVER.Your score is "+str(score))
    window.fill(config.BACKGROUND_COLOR)
    Game_over_text=pygame.font.SysFont(config.GAME_FONT, config.FONT_SIZE).render(
            f"GAME OVER.Your score is {score}", True, config.FONT_COLOR)
    window.blit(Game_over_text,(0,config.GAME_RES[1]//2))      
    #pygame.quit()
    #sys.exit()


def generate_apple(game_res, snake_size):
    x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
    y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
    return [x, y]


def is_collision(snake_head, position):
    if snake_head[0] == position[0] and snake_head[1] == position[1]:
        return True
    return False


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(config.GAME_RES)

    
    snake = [[config.GAME_RES[0]//2, config.GAME_RES[1]//2]]
    apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
    direction = "LEFT"
    score=0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        direction = update_direction(direction, keys)
        new_position = update_position(snake[0], direction, config.SNAKE_SIZE)
        snake.insert(0, new_position)
        if is_collision(snake[0], apple):
            print("Collision")
            apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
            score+=1        
        else:
            snake.pop()

        if is_out(snake[0], config.GAME_RES):
            game_over(window)
        
        for part in snake:
            pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(
                part[0], part[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        
        for part in snake[1:len(snake)]:
            if(is_collision(snake[0],part)):
                game_over(window)
                 

        pygame.draw.rect(window, config.APPLE_COLOR, pygame.Rect(
            apple[0], apple[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        score_text = pygame.font.SysFont(config.GAME_FONT, config.FONT_SIZE).render(
            f"Score {score}", True, config.FONT_COLOR)
        window.blit(score_text,(0,0))    
        pygame.display.update()
        window.fill(config.BACKGROUND_COLOR)
        clock.tick(config.GAME_FPS)