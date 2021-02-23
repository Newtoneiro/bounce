import pygame
from constants import WIDTH, HEIGHT, black, red, blue
from classes import Ball, Table

FPS = 120

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('bounce')

clock = pygame.time.Clock()

def main():
    run = True
    ball1 = Ball(WIN, red, 500, 500, 50, 10, [0, 0])
    ball2 = Ball(WIN, blue, 500, 500, 20, 10, [0, 0])
    table = Table(WIN, [ball1])
    held_object = None
    time = 0
    startx = 0
    starty = 0


    while run:
        clock.tick(FPS)

        if held_object:
            time += 1


        WIN.fill(black)
        table.update()
        for event in pygame.event.get():
            if not held_object:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for obj in table.objects:
                        if (x-obj.x)**2 + (y-obj.y)**2 <= obj.radius**2:
                            startx = x
                            starty = y
                            held_object = obj
                            obj.change_hold()
            if held_object:
                x, y = pygame.mouse.get_pos()
                obj.x, obj.y = x, y

                if event.type == pygame.MOUSEBUTTONUP:
                    obj.V = [0.1*(x - startx)/(0.01*time), 0.1*(y - starty)/(0.01*time)]
                    time = 0
                    startx = starty = 0
                    obj.change_hold()
                    held_object = None

        pygame.display.update()

if __name__ == "__main__":
    main()