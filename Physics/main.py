import pygame
import sys
import pymunk


def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 43)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        # pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 80)
        apple_rect = apple_surface.get_rect(center=(pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape


def draw_static_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (217, 98, 119), (pos_x, pos_y), 50)


pygame.init()
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Physics Lab")
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 500)
apple_surface = pygame.image.load('apple_red.png')
apples = []
balls = []
balls.append(static_ball(space, (900, 500)))
balls.append(static_ball(space, (950, 600)))

while True:
    for event in pygame.event.get():
        Key = pygame.key
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     apples.append(create_apple(space, event.pos))
        # if event.type == pygame.K_s:
        #     balls.append(static_ball(space, event.pos))
        if pygame.mouse.get_pressed()[0]:
            apples.append(create_apple(space, event.pos))
        if pygame.mouse.get_pressed()[2]:
            balls.append(static_ball(space, event.pos))

    screen.fill((217, 217, 217))
    draw_apples(apples)
    draw_static_balls(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
